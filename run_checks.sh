#!/bin/bash

isort run.py
black run.py
flake8 run.py
mypy run.py
