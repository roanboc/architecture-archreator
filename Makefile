# The bench. One target for what a contributor runs before pushing, and one
# for each of the method's reading tools, which live in the archreator plugin
# and not here. Nothing below is required — every recipe is a command anybody
# could paste — but nobody should have to remember where the plugin is.
#
# The plugin is fetched under .archreator/, where everything the method
# generates already lands: gitignored, and skipped by both validators.

ARCHREATOR ?= .archreator/method
METHOD_REF ?= main
METHOD_URL ?= https://github.com/roanboc/archreator

TOOLS  = $(ARCHREATOR)/plugins/archreator/scripts
MODEL  = python3 $(TOOLS)/model.py
BRIEF  = python3 $(TOOLS)/build_brief.py
MKDOCS = uvx --with mkdocs-material mkdocs

# Which tree, which element, which focus. Both trees own a `BSVC1`, so a
# question about one element carries --scope beside --project.
P ?= product-archreator
E ?= BSVC1
F ?= impact
TREES = org-archreator product-archreator

.PHONY: help check method sync trace coverage inventory export brief portal serve smoke clean

help:
	@grep -E '^[a-z]+:.*## ' $(MAKEFILE_LIST) | sed 's/:.*## /  —  /'

check: ## the two validators, exactly as CI runs them
	python3 scripts/check_links.py
	python3 scripts/check_model.py

method: ## fetch the method under .archreator/method, or refresh it
ifeq ($(ARCHREATOR),.archreator/method)
	@if [ -d "$(ARCHREATOR)/.git" ]; then git -C "$(ARCHREATOR)" pull -q --ff-only; \
	else git clone -q --depth 1 --branch "$(METHOD_REF)" "$(METHOD_URL)" "$(ARCHREATOR)"; fi
endif
	@echo "method: $(ARCHREATOR) at $$(git -C '$(ARCHREATOR)' log -1 --format='%h — %s')"

sync: ## the validators here are the scaffold's, byte for byte
	@for f in check_links.py check_model.py model_graph.py element-prefixes.json; do \
	  if cmp -s "$(ARCHREATOR)/plugins/archreator/scaffold/scripts/$$f" "scripts/$$f"; \
	  then echo "  same   scripts/$$f"; \
	  else echo "  DRIFT  scripts/$$f differs from the scaffold's copy — copy it across"; drift=1; fi; \
	done; [ -z "$$drift" ]

trace: ## what a change to E in P would touch
	$(MODEL) --project $(P) trace $(E) --scope $(P)

coverage: ## what is grounded, and what is not yet approved — every tree
	$(MODEL) --project $(P) coverage

inventory: ## one line per element, every tree, stable enough to diff
	$(MODEL) --project $(P) inventory

export: ## model.json of every tree, for a consumer that cannot read Markdown
	$(MODEL) --project $(P) export

brief: ## one disposable brief about E in P, with focus F
	$(BRIEF) --project $(P) --scope $(P) --element $(E) --focus $(F)

portal: ## P as a MkDocs site, built under P/.archreator/work/portal/
	$(MODEL) --project $(P) portal
	$(MKDOCS) build -f $(P)/.archreator/work/portal/mkdocs.yml

serve: portal ## the same site, served locally
	$(MKDOCS) serve -f $(P)/.archreator/work/portal/mkdocs.yml

smoke: check sync ## everything above, non-interactively, over both trees
	@for t in $(TREES); do \
	  echo "== $$t"; \
	  n=$$($(MODEL) --project $$t inventory | wc -l); [ "$$n" -gt 0 ] || exit 1; \
	  echo "  $$n element(s) in the inventory"; \
	  $(MODEL) --project $$t coverage > /dev/null || exit 1; echo "  coverage reads"; \
	  $(BRIEF) --project $$t --scope $$t --element BSVC1 --focus impact > /dev/null || exit 1; echo "  a brief writes"; \
	  $(MODEL) --project $$t portal > /dev/null || exit 1; \
	  $(MKDOCS) build -q -f $$t/.archreator/work/portal/mkdocs.yml || exit 1; echo "  the portal builds"; \
	done
	@$(MODEL) --project product-archreator trace ACMP4 --scope product-archreator > /dev/null && echo "== trace walks"
	@$(MODEL) --project product-archreator export > /dev/null && echo "== export writes .model/model.json"

clean: ## everything generated — the method checkout stays
	rm -rf .model $(addsuffix /.archreator/work,$(TREES))
