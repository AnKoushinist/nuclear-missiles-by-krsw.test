#!/bin/bash

cat .gitlab-ci.header.yml > .gitlab-ci.yml

for i in "$@"; do
  cat .gitlab-ci.section.yml | sed -e "s/NAME/$i/" >> .gitlab-ci.yml
done
