CSV_FILES = \
  data/african-group.csv \
  data/annex-one.csv \
  data/aosis.csv \
  data/arab-group.csv \
  data/asia-pacific-group.csv \
  data/brics.csv \
  data/eig.csv \
  data/eastern-european-group.csv \
  data/european-union.csv \
  data/g20.csv \
  data/g7.csv \
  data/g77.csv \
  data/graduated-ldcs.csv \
  data/ldcs.csv \
  data/non-annex-one.csv \
  data/oecd.csv \
  data/opec.csv \
  data/sids-non-un-or-regional-commissions-associates.csv \
  data/sids.csv \
  data/umbrella.csv \
  data/unfccc.csv

all: $(CSV_FILES) countrygroups/__init__.py index.js

data/%.csv: scripts/%.py scripts/util.py venv
	@echo $@
	@./venv/bin/python $<

index.js countrygroups/__init__.py: scripts/generate_modules.py $(CSV_FILES) datapackage.json
	@echo $@
	@./venv/bin/python $<

venv: scripts/requirements.txt
	[ -d ./venv ] || python3 -m venv venv
	./venv/bin/pip install --upgrade pip
	./venv/bin/pip install -Ur $<
	touch venv

clean-generated-files:
	rm -rf index.js data/*.csv

clean-venv:
	rm -rf venv

clean: clean-generated-files clean-venv

tag:
	./scripts/create_tag.sh

.PHONY: clean clean-generated-files clean-venv tag
