#!/usr/bin/env python

import uproot
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path1="/storage/epp2/phshgg/Public/ew_analyses/run3_tuples/17/d13600GeV_block7_Down_Full_Stream.root:WpNoMuID/DecayTree"

with uproot.open(path1) as t:
    momenta_pos = t.arrays(["mu_PX","mu_PY","mu_PZ"],library="pd")

path2="/storage/epp2/phshgg/Public/ew_analyses/run3_tuples/17/d13600GeV_block7_Down_Full_Stream.root:WmNoMuID/DecayTree"

with uproot.open(path2) as t:
    momenta_neg = t.arrays(["mu_PX","mu_PY","mu_PZ"],library="pd")

momenta_pos['mu_PT'] = np.sqrt(momenta_pos['mu_PX']**2 + momenta_pos['mu_PY']**2)
momenta_neg['mu_PT'] = np.sqrt(momenta_neg['mu_PX']**2 + momenta_neg['mu_PY']**2)

print(f"W+ p_T max = {momenta_pos['mu_PT'].max()}")
print(f"W+ p_T med = {momenta_pos['mu_PT'].median()}")
print(f"W+ p_T min = {momenta_pos['mu_PT'].min()}")

momenta_pos['mu_PT'] = momenta_pos['mu_PT']/1e3
momenta_neg['mu_PT'] = momenta_neg['mu_PT']/1e3

print(f'Number of W+ events: {momenta_pos.shape[0]}')
print(f'Number of W- events: {momenta_neg.shape[0]}')

plt.figure()
plt.hist(x=momenta_pos['mu_PT'], bins=100, range= [momenta_pos['mu_PT'].min(),0.04e3])
plt.xlabel(r'Transverse Momentum / [$Gev/c$]')
plt.ylabel('Events')
plt.savefig('transient/Wp_PT.png', dpi = 300, bbox_inches='tight')
plt.show()

plt.figure()
plt.hist(x=momenta_neg['mu_PT'], bins=100 , range = [momenta_neg['mu_PT'].min(),0.04e3], color='orange')
plt.xlabel(r'Transverse Momentum / [$Gev/c$] ')
plt.ylabel('Events')
plt.savefig('transient/Wm_PT.png', dpi = 300, bbox_inches='tight')
plt.show()

plt.figure()
plt.hist(x=momenta_pos['mu_PT'], bins=100)
plt.hist(x=momenta_neg['mu_PT'], bins=100)
plt.xlabel(r'Transverse Momentum / [$Gev/c$]')
plt.ylabel('Events')
plt.savefig('transient/Wjoint_PT.png', dpi = 300, bbox_inches='tight')
plt.show()

edges = np.linspace(0, 100, 51)

A, _ = np.histogram(momenta_pos['mu_PT'], bins=edges)
B, _ = np.histogram(momenta_neg['mu_PT'], bins=edges)

total = A + B
asymmetry = np.divide(
    A - B,
    total,
    out = np.full(total.shape, np.nan),
    where = total > 0
)

centres = (edges[:-1] + edges[1:]) / 2

plt.figure()
plt.plot(centres, asymmetry, ".")
plt.axhline(0, color="grey", linestyle="--")
plt.xlabel(r"Muon $p_T$ [GeV/$c$]")
plt.ylabel(r"$(W_+ - W_-)/(W_+ + W_-)$")
plt.savefig('transient/Wjoint_asym.png', dpi = 300, bbox_inches='tight')
plt.show()

#convert to float before calc
A = A.astype(float)
B = B.astype(float)

#update total to float
total = A + B
valid = total > 0

asymmetry2 = (A[valid] - B[valid]) / total[valid]
error = np.sqrt(4 * A[valid] * B[valid] / total[valid] ** 3)

plt.figure()
plt.errorbar(
    centres[valid], asymmetry2,
    yerr=error, fmt=".", capsize=2
)
plt.axhline(0, color="grey", linestyle="--")
plt.xlabel(r"Muon $p_T$ [GeV/$c$]")
plt.ylabel(r"$(W_+ - W_-)/(W_+ + W_-)$")
plt.savefig('transient/Wjoint_asym_error.png', dpi = 300, bbox_inches='tight')
plt.show()

