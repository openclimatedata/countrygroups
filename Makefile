CSV_FILES = data/unfccc.csv data/annex-one.csv data/non-annex-one.csv data/ldcs.csv data/graduated-ldcs.csv data/eu-member-states.csv data/sids.csv data/sids-non-un-or-regional-commissions-associates.csv data/g20.csv data/g7.csv data/oecd.csv data/brics.csv data/umbrella.csv data/opec.csv data/aosis.csv data/eig.csv

all: $(CSV_FILES) unfccc_groups/__init__.py index.js

data/unfccc.csv: scripts/unfccc.py venv
	@echo $@
	@./venv/bin/python $<

data/annex-one.csv: scripts/annex-one.py venv
	@echo $@
	@./venv/bin/python $<

data/non-annex-one.csv: scripts/non-annex-one.py venv
	@echo $@
	@./venv/bin/python $<

data/ldcs.csv data/graduated-ldcs.csv: scripts/ldcs.py
	@echo $@
	@./venv/bin/python $<

data/eu-member-states.csv: scripts/eu-member-states.py
	@echo $@
	@./venv/bin/python $<

data/sids.csv data/sids-non-un-or-regional-commissions-associates.csv: scripts/sids.py
	@echo $@
	@./venv/bin/python $<

data/g20.csv: scripts/g20.py
	@echo $@
	@./venv/bin/python $<

data/g7.csv: scripts/g7.py
	@echo $@
	@./venv/bin/python $<

data/oecd.csv: scripts/oecd.py
	@echo $@
	@./venv/bin/python $<

data/brics.csv: scripts/brics.py
	@echo $@
	@./venv/bin/python $<

data/umbrella.csv: scripts/umbrella.py
	@echo $@
	@./venv/bin/python $<

data/opec.csv: scripts/opec.py
	@echo $@
	@./venv/bin/python $<

data/aosis.csv: scripts/aosis.py
	@echo $@
	@./venv/bin/python $<

data/eig.csv: scripts/eig.py
	@echo $@
	@./venv/bin/python $<

index.js unfccc_groups/__init__.py: scripts/generate_modules.py $(CSV_FILES) datapackage.json
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
