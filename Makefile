CSV_FILES = \
  data/annex-one.csv \
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
  data/ldcs.csv \
  data/non-annex-one.csv \
  data/oecd.csv \
  data/opec.csv \
  data/sids-non-un-or-regional-commissions-associates.csv \
  data/sids.csv \
  data/ssp.csv \
  data/umbrella.csv \
  data/unfccc.csv \
  data/un-regional-groups.csv

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
	rm -rf index.js data/*.csv countrygroups/__init__.py

clean-venv:
	rm -rf venv

clean: clean-generated-files clean-venv

tag:
	./scripts/create_tag.sh

publish-on-pypi:
	@status=$$(git status --porcelain); \
	if test "x$${status}" = x; then \
		python setup.py bdist_wheel --universal; \
		twine upload dist/*; \
	else \
		echo Working directory is dirty >&2; \
	fi;

publish-on-test-pypi:
	@status=$$(git status --porcelain); \
	if test "x$${status}" = x; then \
		python setup.py bdist_wheel --universal; \
		twine upload -r testpypi dist/*; \
	else \
		echo Working directory is dirty >&2; \
	fi;

test-pypi-install:
	$(eval TEMPVENV := $(shell mktemp -d))
	python3 -m venv $(TEMPVENV)
	$(TEMPVENV)/bin/pip install pip --upgrade
	$(TEMPVENV)/bin/pip install countrygroups
	$(TEMPVENV)/bin/python -c "import sys; sys.path.remove(''); import countrygroups; print(countrygroups.__version__)"


.PHONY: clean clean-generated-files clean-venv tag publish-on-pypi publish-on-test-pypi test-pypi-install
