CSV_FILES = \
  data/aosis.csv \
  data/ar5.csv \
  data/arab-group.csv \
  data/brics.csv \
  data/eig.csv \
  data/european-union.csv \
  data/g20.csv \
  data/g77.csv \
  data/g7.csv \
  data/graduated-ldcs.csv \
  data/imo.csv \
  data/ldc.csv \
  data/lldc.csv \
  data/oecd.csv \
  data/opec.csv \
  data/sids-non-un-or-regional-commissions-associates.csv \
  data/sids.csv \
  data/ssp.csv \
  data/umbrella.csv \
  data/unfccc.csv \
  data/un-regional-groups.csv

# Website currently down.
	#data/annex-one.csv \
	#data/annex-one-kaz.csv \
	#data/non-annex-one.csv \


JSON_FILES = \
  data/unstats-geographical-regions.json

all: $(CSV_FILES) py/countrygroups/__init__.py index.js

data/%.csv: scripts/%.py scripts/util.py venv
	@echo $@
	@./venv/bin/python $<

data/%.json: scripts/%.py scripts/util.py venv
	@echo $@
	@./venv/bin/python $<

index.js py/countrygroups/__init__.py: scripts/generate_modules.py $(CSV_FILES) $(JSON_FILES) datapackage.json
	@echo $@
	@./venv/bin/python $<

venv: scripts/requirements.txt
	[ -d ./venv ] || python3 -m venv venv
	./venv/bin/pip install --upgrade pip
	./venv/bin/pip install -Ur $<
	touch venv

clean-generated-files:
	rm -rf js/index.js data/*.csv data/*.json py/countrygroups/__init__.py

clean-venv:
	rm -rf venv

clean: clean-generated-files clean-venv

tag:
	./scripts/create_tag.sh

publish-on-pypi:
	./scripts/publish-on-pypi.sh

publish-on-test-pypi:
	./scripts/publish-on-test-pypi.sh

test-pypi-install:
	$(eval TEMPVENV := $(shell mktemp -d))
	python3 -m venv $(TEMPVENV)
	$(TEMPVENV)/bin/pip install pip --upgrade
	$(TEMPVENV)/bin/pip install countrygroups
	$(TEMPVENV)/bin/python -c "import sys; sys.path.remove(''); import countrygroups; print(countrygroups.__version__)"

validate:
	./venv/bin/python scripts/validate.py

.PHONY: clean clean-generated-files clean-venv tag publish-on-pypi publish-on-test-pypi test-pypi-install
