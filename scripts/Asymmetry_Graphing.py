#!/usr/bin/env python

import uproot
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import h5py
import os

with h5py.File('transient/Asymmetry_analysis.h5', 'r') as f:
    edges     = f['edges'][:]
    Wp_counts = f['Wp_counts'][:]
    Wm_counts = f['Wm_counts'][:]
    A         = f['A'][:]
    sigma_A   = f['sigma_A'][:]

width=edges[1]-edges[0]
centers = edges+(width/2)

plt.figure()
plt.bar(edges, Wp_counts/100000, width=width, align='edge',color='red',label='Wp')
plt.bar(edges, Wm_counts/100000, width=width, align='edge',color='blue',label='Wm')
plt.xlabel('Transverse Momenta [GeV]')
plt.ylabel('Counts [10e5]')
plt.legend()
plt.savefig('transient/Combined_Transverse_Momenta.png')

plt.figure()
plt.errorbar(centers,A,yerr=sigma_A,fmt='o',capsize=4,ecolor='black',elinewidth=1,markersize=6)
plt.xlabel('Transverse Momenta [GeV]')
plt.ylabel('Asymmetry')
plt.savefig('transient/Asymmetry.png')

print('Done')
