#!/usr/bin/env python

import uproot
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

DATADIR="/storage/epp2/phshgg/Public/ew_analyses/run3_tuples/17/d13600GeV_block7_Down_Full_Stream.root"

with uproot.open(f"{DATADIR}:WmNoMuID/DecayTree") as t:
        Wm_momenta = t.arrays(["mu_PX","mu_PY","mu_PZ"],library="np")

Wm_mu_PX = Wm_momenta["mu_PX"]
Wm_mu_PY = Wm_momenta["mu_PY"]
Wm_mu_PZ = Wm_momenta["mu_PZ"]

with uproot.open(f"{DATADIR}:WpNoMuID/DecayTree") as t:
        Wp_momenta = t.arrays(["mu_PX","mu_PY","mu_PZ"],library="np")

Wp_mu_PX = Wp_momenta["mu_PX"]
Wp_mu_PY = Wp_momenta["mu_PY"]
Wp_mu_PZ = Wp_momenta["mu_PZ"]

Wm_mu_Pt = np.sqrt(Wm_mu_PX**2+Wm_mu_PY**2)
Wp_mu_Pt = np.sqrt(Wp_mu_PX**2+Wp_mu_PY**2)

Wm_counts, Wm_edges = np.histogram(Wm_mu_Pt/1000,bins=50,range=(15, 50))
Wp_counts, Wp_edges = np.histogram(Wp_mu_Pt/1000,bins=50,range=(15, 50))

def path(direct):
        return(os.path.expanduser(f'~/transient/{direct}'))

def asymmetry(A,B):
        f=(A-B)/(A+B)
        sigma_A=np.sqrt(A)
        sigma_B=np.sqrt(B)

        df_dA=2*B/((A+B)**2)
        df_dB=-2*A/((A+B)**2)

        var_f=[]
        for i in range(len(A)):

                C=np.array([[A[i],0],
                [0,B[i]]])
                J=np.array([df_dA[i],df_dB[i]])
                var_f.append(J@C@J.T)

        sigma_f=np.sqrt(np.array(var_f))

        return f, sigma_f

A, sigma_A=asymmetry(Wp_counts,Wm_counts)

np.savetxt(path('Asymmetry_analysis.txt'),np.column_stack([Wm_edges[:-1], Wp_counts,Wm_counts,A,sigma_A]),fmt='%e')

print('Done')
