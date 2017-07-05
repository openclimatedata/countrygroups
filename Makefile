all: process

process: scripts/process.py venv
	./venv/bin/python $<

venv: scripts/requirements.txt
	[ -d ./venv ] || python3 -m venv venv
	./venv/bin/pip install --upgrade pip
	./venv/bin/pip install -Ur $<
	touch venv

clean:
	rm -rf data/*.csv venv

.PHONY: clean
