#!/usr/bin/env python

import uproot
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import h5py

DATADIR={
        'measurement':"/storage/epp2/phshgg/Public/ew_analyses/run3_tuples/17/d13600GeV_block7_Down_Full_Stream.root",
        'simulation':"transient/event_data.root"
        }

for g in DATADIR:
	if g=='measurement':
		with uproot.open(f"{DATADIR[g]}:WmNoMuID/DecayTree") as t:
			Wm_momenta = t.arrays(["mu_PX","mu_PY","mu_PZ"],library="np")

		Wm_mu_PX = Wm_momenta["mu_PX"]
		Wm_mu_PY = Wm_momenta["mu_PY"]
		Wm_mu_PZ = Wm_momenta["mu_PZ"]

		with uproot.open(f"{DATADIR[g]}:WpNoMuID/DecayTree") as t:
		        Wp_momenta = t.arrays(["mu_PX","mu_PY","mu_PZ"],library="np")

		Wp_mu_PX = Wp_momenta["mu_PX"]
		Wp_mu_PY = Wp_momenta["mu_PY"]
		Wp_mu_PZ = Wp_momenta["mu_PZ"]

		Wm_mu_Pt = np.sqrt(Wm_mu_PX**2+Wm_mu_PY**2)/1000
		Wp_mu_Pt = np.sqrt(Wp_mu_PX**2+Wp_mu_PY**2)/1000

	if g=='simulation':
		with uproot.open(f'{DATADIR[g]}:Events;1') as t:
			df = t.arrays(["pT_GeV", "charge"],library="np")

		pT_GeV=df["pT_GeV"]
		charge=df["charge"]

		Wm=[]
		Wp=[]
		for i in range(len(charge)):
			if charge[i]==-1:
				Wm.append(pT_GeV[i])
			if charge[i]==1:
				Wp.append(pT_GeV[i])

		Wm_mu_Pt = np.array(Wm)
		Wp_mu_Pt = np.array(Wp)

	Wm_counts, Wm_edges = np.histogram(Wm_mu_Pt,bins=50,range=(15, 50))
	Wp_counts, Wp_edges = np.histogram(Wp_mu_Pt,bins=50,range=(15, 50))

	def asymmetry(A,B):
		f=np.zeros(len(A))
		sigma_f=np.zeros(len(A))
		for i in range(len(A)):

			if ((A[i]+B[i]) == 0) or (4*A[i]*B[i]/((A[i]+B[i])**3)<0):
				f[i]=np.nan
				sigma_f[i]=np.nan

			else:

				f[i]=(A[i]-B[i])/(A[i]+B[i])
				sigma_f[i]=np.sqrt(4*A[i]*B[i]/((A[i]+B[i])**3))

		return f, sigma_f

	A, sigma_A=asymmetry(Wp_counts,Wm_counts)

	with h5py.File(f'transient/Asymmetry_{g}.h5', 'w') as f:
		f.create_dataset('edges',     data=Wm_edges[:-1])
		f.create_dataset('Wp_counts', data=Wp_counts)
		f.create_dataset('Wm_counts', data=Wm_counts)
		f.create_dataset('A',         data=A)
		f.create_dataset('sigma_A',   data=sigma_A)

print('Done')
