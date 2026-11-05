#!/usr/bin/env python

import uproot
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

def path(direct):
        return(os.path.expanduser(f'~/transient/{direct}'))

data = np.loadtxt(path('Asymmetry_analysis.csv'), delimiter=',', skiprows=1)

edges, Wp_counts, Wm_counts, A, sigma_A = data.T

width=edges[1]-edges[0]
centers = edges+(width/2)

plt.figure()
plt.bar(edges, Wp_counts/100000, width=width, align='edge',color='red',label='Wp')
plt.bar(edges, Wm_counts/100000, width=width, align='edge',color='blue',label='Wm')
plt.xlabel('Transverse Momenta [GeV]')
plt.ylabel('Counts [10e5]')
plt.legend()
plt.savefig(path('Combined_Transverse_Momenta.png'))

plt.figure()
plt.errorbar(centers,A,yerr=sigma_A,fmt='o',capsize=4,ecolor='black',elinewidth=1,markersize=6)
plt.xlabel('Transverse Momenta [GeV]')
plt.ylabel('Asymmetry')
plt.savefig(path('Asymmetry.png'))

print('Done')
