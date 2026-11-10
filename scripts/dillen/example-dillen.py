#!/usr/bin/env python

import uproot
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

DATADIR="/storage/epp2/phshgg/Public/ew_analyses/run3_tuples/11/"

with uproot.open(f"{DATADIR}/d13600GeV_24c3_Up_Turbo_Stream.root:U1S/DecayTree") as t:

    momenta = t.arrays(["mup_PX","mup_PY","mup_PZ","mum_PX","mum_PY","mum_PZ"],library="pd").astype('float64')

    momenta['mup_p'] = np.sqrt((momenta['mup_PX']**2 + momenta['mup_PY']**2 + momenta['mup_PZ']**2 ))
    momenta['mum_p'] = np.sqrt((momenta['mum_PX']**2 + momenta['mum_PY']**2 + momenta['mum_PZ']**2 ))

    mass = 105.66 # MeV

    momenta['E_mup'] = np.sqrt((momenta['mup_p']**2 + mass**2))
    momenta['E_mum'] = np.sqrt((momenta['mum_p']**2 + mass**2))

    p_total_sqrd = (momenta['mup_PX'] + momenta['mum_PX'])**2 + (momenta['mup_PY'] + momenta['mum_PY'])**2 + (momenta['mup_PZ'] + momenta['mum_PZ'])**2

    momenta['U1S_M'] = np.sqrt((momenta['E_mup'] + momenta['E_mum'])**2 - p_total_sqrd)

    plt.hist(x=momenta['U1S_M'], bins=150, range=[8500,10500] )
    plt.xlabel('Invariant Mass / [Mev/$c^2$]')
    plt.ylabel('Events')
    plt.savefig('transient/U1S_mass4.png', dpi = 300, bbox_inches='tight')
    plt.show()

    print(momenta.head())

