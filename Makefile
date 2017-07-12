CSV_FILES = data/unfccc.csv data/annex-one.csv data/non-annex-one.csv data/ldcs.csv data/graduated-ldcs.csv data/eu-member-states.csv data/sids.csv data/sids-non-un-or-regional-commissions-associates.csv data/g20.csv data/g7.csv data/oecd.csv data/brics.csv data/umbrella.csv data/opec.csv data/aosis.csv data/eig.csv data/g77.csv

all: $(CSV_FILES) countrygroups/__init__.py index.js

data/%.csv: scripts/%.py venv
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
