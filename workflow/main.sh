#!/bin/bash

# step 1 generate events with pythia
./run-pythia

# step 2 asymmetry measurement
./scripts/Asymmetry.py

# step 3 graphing
./scripts/Plotting.py
