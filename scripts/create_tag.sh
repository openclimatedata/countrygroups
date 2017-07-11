#!/usr/bin/env bash

if [[ `git status --porcelain` ]]; then
  printf "Working directory not clean:\n\n"
  git status
else
  echo Current tags:
  git tag
  echo "Please enter next version (x.y.z):"
  read version
  echo "You entered: $version"
  npm version $version
fi
