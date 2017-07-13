#!/usr/bin/env bash

if [[ `git status --porcelain` ]]; then
  printf "Working directory not clean:\n\n"
  git status
else
  echo Current tags:
  git tag

  echo Commits since last tag:
  git log `git describe --tags --abbrev=0`..HEAD --oneline
  echo "Please enter next version (x.y.z):"
  read version
  echo "You entered: $version"
  sed -i -r "s/(\"version\": \").*(\")/\1$version\2/" datapackage.json
  git add datapackage.json
  git commit -m "Update version in datapackage.json"
  npm version $version
fi
