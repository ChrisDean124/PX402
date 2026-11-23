#!/bin/bash

# step 1 generate N events with pythia: ./run-pythia N
./run-pythia 5000

# step 2 asymmetry measurement
./scripts/Asymmetry.py

# step 3 graphing
./scripts/Plotting.py
