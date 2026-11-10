columns in df:

['BUNCHCROSSING_ID', 'BUNCHCROSSING_TYPE', 'EVENTNUMBER', 'GPSTIME', 'Hlt1SingleHighPtMuonDecision', 'Hlt1SingleHighPtMuonNoMuIDDecision', 'Hlt1_TCK', 'Hlt2QEE_SingleHighPtMuonFullDecision', 'Hlt2QEE_SingleHighPtMuonNoMuIDFullDecision', 'Hlt2QEE_ZToMuMuFullDecision', 'Hlt2QEE_ZToMuMu_SingleNoMuIDFullDecision', 'Hlt2TrackEff_ZToMuMu_Downstream_mum_MatchDecision', 'Hlt2TrackEff_ZToMuMu_Downstream_mum_TagDecision', 'Hlt2TrackEff_ZToMuMu_Downstream_mup_MatchDecision', 'Hlt2TrackEff_ZToMuMu_Downstream_mup_TagDecision', 'Hlt2TrackEff_ZToMuMu_MuonUT_mum_MatchDecision', 'Hlt2TrackEff_ZToMuMu_MuonUT_mum_TagDecision', 'Hlt2TrackEff_ZToMuMu_MuonUT_mup_MatchDecision', 'Hlt2TrackEff_ZToMuMu_MuonUT_mup_TagDecision', 'Hlt2TrackEff_ZToMuMu_SeedMuon_mum_MatchDecision', 'Hlt2TrackEff_ZToMuMu_SeedMuon_mum_TagDecision', 'Hlt2TrackEff_ZToMuMu_SeedMuon_mup_MatchDecision', 'Hlt2TrackEff_ZToMuMu_SeedMuon_mup_TagDecision', 'Hlt2TrackEff_ZToMuMu_VeloMuon_mum_MatchDecision', 'Hlt2TrackEff_ZToMuMu_VeloMuon_mum_TagDecision', 'Hlt2TrackEff_ZToMuMu_VeloMuon_mup_MatchDecision', 'Hlt2TrackEff_ZToMuMu_VeloMuon_mup_TagDecision', 'Hlt2_TCK', 'ODINTCK', 'RUNNUMBER', 'hCalTot', 'isMC', 'nEcalClusters', 'nFTClusters', 'nLongTracks', 'nPVs', 'nVPClusters', 'polarity_sign', 'year_int', 'U1S_ENDVCHI2', 'U1S_ENDVCHI2DOF', 'U1S_PID', 'U1S_Hlt1SingleHighPtMuonDecision_TOS', 'U1S_Hlt1SingleHighPtMuonNoMuIDDecision_TOS', 'U1S_Hlt1SingleHighPtMuonDecision_TIS', 'U1S_Hlt1SingleHighPtMuonNoMuIDDecision_TIS', 'mum_BPVIP', 'mum_BPVIPCHI2', 'mum_TRCHI2NDOF', 'mum_PV_X', 'mum_PV_Y', 'mum_PV_Z', 'mum_Q', 'mum_PX', 'mum_PY', 'mum_PZ', 'mum_ISMUON', 'mum_INMUON', 'mum_PIDmu', 'mum_HCALEOP', 'mum_ECALEOP', 'mum_PID', 'mum_Hlt1SingleHighPtMuonDecision_TOS', 'mum_Hlt1SingleHighPtMuonNoMuIDDecision_TOS', 'mum_Hlt1SingleHighPtMuonDecision_TIS', 'mum_Hlt1SingleHighPtMuonNoMuIDDecision_TIS', 'mup_BPVIP', 'mup_BPVIPCHI2', 'mup_TRCHI2NDOF', 'mup_PV_X', 'mup_PV_Y', 'mup_PV_Z', 'mup_Q', 'mup_PX', 'mup_PY', 'mup_PZ', 'mup_ISMUON', 'mup_INMUON', 'mup_PIDmu', 'mup_HCALEOP', 'mup_ECALEOP', 'mup_PID', 'mup_Hlt1SingleHighPtMuonDecision_TOS', 'mup_Hlt1SingleHighPtMuonNoMuIDDecision_TOS', 'mup_Hlt1SingleHighPtMuonDecision_TIS', 'mup_Hlt1SingleHighPtMuonNoMuIDDecision_TIS']

26.10.26:
-summary on U1S process and why transverse momentum important (less variation than parallel)

next steps:
-hadronic background modelling:
-replace p with m in string to get minus charge
-use GeV instead of MeV, overlay plots for two charges
-plot the 'asymmetry': (A - B) / (A + B) where A, B are the values of transverse momentum
-for error bars, f(x,y) = (x-y)/(x+y)
-Var(f) = JCJ^T (J is jacobian, C is covariance matrix)
-May see bump around middle as the decay signal at mv/2
-there will likely be a statistically significant non-zero asymmetry because the counts plot is essentially an integrated cross-section