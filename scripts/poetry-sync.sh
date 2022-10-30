#!/bin/bash

cd $(dirname $0)/..

poetry export -f requirements.txt --output requirements.txt
poetry export -f requirements.txt --with dev --output requirements.dev.txt
