#!/usr/bin/env python

import uproot
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import time
import os
import h5py

DATADIR={
        'experimental':"/storage/epp2/phshgg/Public/ew_analyses/run3_tuples/17/d13600GeV_block7_Down_Full_Stream.root",
        'prediction':"/storage/physics/phupzd/project/data/output_data.root"
        }

etamin=2.0
etamax=4.5

for g in DATADIR:
	if g=='experimental':
		with uproot.open(f"{DATADIR[g]}:WmNoMuID/DecayTree") as t:
			Wm_momenta = t.arrays(["mu_PX","mu_PY","mu_PZ"],library="np")
			#print(t.keys())
		Wm_mu_PX = Wm_momenta["mu_PX"]/1000
		Wm_mu_PY = Wm_momenta["mu_PY"]/1000
		Wm_mu_PZ = Wm_momenta["mu_PZ"]/1000

		with uproot.open(f"{DATADIR[g]}:WpNoMuID/DecayTree") as t:
		        Wp_momenta = t.arrays(["mu_PX","mu_PY","mu_PZ"],library="np")

		Wp_mu_PX = Wp_momenta["mu_PX"]/1000
		Wp_mu_PY = Wp_momenta["mu_PY"]/1000
		Wp_mu_PZ = Wp_momenta["mu_PZ"]/1000

		Wm_mu_P = np.sqrt(Wm_mu_PX**2+Wm_mu_PY**2+Wm_mu_PZ**2)
		Wp_mu_P = np.sqrt(Wp_mu_PX**2+Wp_mu_PY**2+Wp_mu_PZ**2)

		Wm_n = np.arctanh(Wm_mu_PZ/Wm_mu_P)
		Wp_n = np.arctanh(Wp_mu_PZ/Wp_mu_P)

		Wm_mask=(etamin<=Wm_n) & (Wm_n<=etamax)
		Wp_mask=(etamin<=Wp_n) & (Wp_n<=etamax)

		Wm_mu_Pt = np.sqrt(Wm_mu_PX[Wm_mask]**2+Wm_mu_PY[Wm_mask]**2)
		Wp_mu_Pt = np.sqrt(Wp_mu_PX[Wp_mask]**2+Wp_mu_PY[Wp_mask]**2)

	if g=='prediction':
		with uproot.open(f'{DATADIR[g]}:Events;1') as t:
			df = t.arrays(["pT_GeV", "charge","eta"],library="pd")
			#print(t.keys())
			#print(df["eta"])
		Wm_mu_Pt = df.loc[(df["charge"] == -1) & (etamin<=df["eta"]) & (etamax>=df["eta"]), "pT_GeV"].to_numpy()
		Wp_mu_Pt = df.loc[(df["charge"] == +1) & (etamin<=df["eta"]) & (etamax>=df["eta"]), "pT_GeV"].to_numpy()

	Wm_counts, Wm_edges = np.histogram(Wm_mu_Pt,bins=20,range=(15, 100))
	Wp_counts, Wp_edges = np.histogram(Wp_mu_Pt,bins=20,range=(15, 100))

	def asymmetry(A,B):

		denom=A+B
		with np.errstate(divide="ignore", invalid="ignore"):
			var_f=(4*A*B)/(denom**3)
			mask=(denom!=0) & (var_f>=0)

			f=np.full_like(A, np.nan, dtype=float)
			sigma_f=np.full_like(A, np.nan, dtype=float)

			f[mask]=(A[mask]-B[mask])/denom[mask]
			sigma_f[mask]=np.sqrt(var_f[mask])

		return f, sigma_f

	A, sigma_A=asymmetry(Wp_counts,Wm_counts)

	with h5py.File(f'transient/Asymmetry_{g}.h5', 'w') as f:
		f.create_dataset('edges',     data=Wm_edges[:-1])
		f.create_dataset('Wp_counts', data=Wp_counts)
		f.create_dataset('Wm_counts', data=Wm_counts)
		f.create_dataset('A',         data=A)
		f.create_dataset('sigma_A',   data=sigma_A)

print('Done')
