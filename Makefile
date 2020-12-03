# Project utility scripts
.PHONY: test

# Setup environment
export SRC_DIR := ./src/python
export TEST_DIR := ./test/python
export PYTHONPATH := ${SRC_DIR}:${TEST_DIR}:${PYTHONPATH}
export PATH := ${TEST_DIR}:${PATH}
export PYTHONWARNINGS := ignore

# Default python executable if not provided
PYTHON ?= python

# Download test data
data: 
	mkdir -p /tmp/txtmarker
	wget -N https://github.com/neuml/txtmarker/releases/download/v0.0.0/tests.tar.gz -P /tmp
	tar -xvzf /tmp/tests.tar.gz -C /tmp

# Unit tests
test:
	${PYTHON} -m unittest discover -v -s ${TEST_DIR}

# Run tests while calculating code coverage
coverage:
	coverage run --source=${SRC_DIR} -m unittest discover -v -s ${TEST_DIR}
