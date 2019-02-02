#!/bin/sh
export PROJECT_HOME="/Users/davidsykes/Git-repos/prop-map"
export PYTHON_PATH="/Users/davidsykes/miniconda3/envs/rightmove/bin/python"

source $PROJECT_HOME/.env

$PYTHON_PATH $PROJECT_HOME/src/scrape_outcodes.py