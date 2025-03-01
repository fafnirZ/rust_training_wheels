#!/bin/bash

cd regex_maturin
maturin build --release -o release

cd ../
cd benchmarker
# run
make develop
uv run hello.py