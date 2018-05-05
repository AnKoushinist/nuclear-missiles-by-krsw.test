#!/bin/bash

ci-script(){

echo 'image: python:3'

echo 'stages:'
seq 1 $1 | while read i ; do echo "- bomb$i" ; done

echo "
.temp: &base
  script:
    - timeout 30m ./py/lambda_function.py
  allow_failure: true
  retry: 2
"

seq 1 $1 | while read i ; do
  echo "
bomb$i:
  <<: *base
  stage: bomb$i
"
done

}

ci-script "$@" > .gitlab-ci.yml
