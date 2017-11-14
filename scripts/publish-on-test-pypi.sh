#!/usr/bin/env bash

rm -rf py/build py/dist
status=$(git status --porcelain);
if test "x${status}" = x; then
  cd py
  ../venv/bin/python setup.py bdist_wheel --universal;
  ../venv/bin/twine upload -r testpypi dist/*;
else
  echo Working directory is dirty >&2;
fi;
