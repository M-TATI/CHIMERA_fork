
#########################
# Some base parameters
#########################

# MASS: lambdaPeak, alpha, beta, deltam, ml, mh, muMass, sigmaMass 
lambda_mass_PLP_mock_v1   = {"lambda_peak":0.039, "alpha":3.4, "beta":1.1, "delta_m":4.8, "ml":5.1, "mh":87., "mu_g":34., "sigma_g":3.6}

# RATE: R0, alphaRedshift , betaRedshift, zp 
lambda_rate_Madau_mock_v1 = {"gamma":1.9,"kappa":3.4,"zp":2.4,}  

# COSMOLOGY: H0, Om0
lambda_cosmo_mock_v1      = {"H0":67.66, "Om0":0.30966}
lambda_cosmo_GLADE        = {"H0":70., "Om0":0.27}
lambda_cosmo_MICEv2       = {"H0":70., "Om0":0.25}
lambda_cosmo_737          = {"H0":70., "Om0":0.3}

#############################
# Lists of observed events
#############################

# All confident events with SNR>8 and FAR>1
list_O1O2_events   = ['GW150914', 'GW170729', 'GW170814', 'GW170809', 'GW151226', 'GW170104', 'GW170818', 'GW151012', 'GW170823', 'GW170608']
list_O3a_events    = ['GW190701_203306', 'GW190413_134308', 'GW190720_000836', 'GW190527_092055', 'GW190708_232457', 'GW190503_185404', 'GW190924_021846', 'GW190413_052954', 
                      'GW190514_065416', 'GW190731_140936', 'GW190828_065509', 'GW190706_222641', 'GW190930_133541', 'GW190408_181802', 'GW190803_022701', 'GW190915_235702', 
                      'GW190728_064510', 'GW190727_060333', 'GW190707_093326', 'GW190828_063405', 'GW190602_175927', 'GW190421_213856', 'GW190521', 'GW190521_074359', 'GW190910_112807', 
                      'GW190519_153544', 'GW190412', 'GW190512_180714', 'GW190630_185205', 'GW190517_055101', 'GW190513_205428', 'GW190929_012149', 'GW190620_030421']
list_O3b_events    = ['GW191222_033537', 'GW200112_155838', 'GW200202_154313', 'GW191216_213338', 'GW191204_171526', 'GW200208_130117', 'GW191230_180458', 'GW200302_015811', 
                      'GW200219_094415', 'GW191215_223052', 'GW191127_050227', 'GW200128_022011', 'GW200225_060421', 'GW200311_115853', 'GW191105_143521', 'GW191103_012549', 
                      'GW200316_215756', 'GW200224_222234', 'GW200129_065458', 'GW191129_134029', 'GW191109_010717', 'GW200216_220804', 'GW200209_085452']

# All confident events with SNR>11 and FAR>1
list_O1O2_events11 = ['GW150914', 'GW170814', 'GW170809', 'GW151226', 'GW170104', 'GW170818', 'GW170823', 'GW170608']
list_O3a_events11  = ['GW190701_203306', 'GW190720_000836', 'GW190708_232457', 'GW190503_185404', 'GW190924_021846', 'GW190828_065509', 'GW190706_222641', 'GW190408_181802', 
                      'GW190915_235702', 'GW190728_064510', 'GW190727_060333', 'GW190707_093326', 'GW190828_063405', 'GW190602_175927', 'GW190521', 'GW190521_074359', 
                      'GW190910_112807', 'GW190519_153544', 'GW190412', 'GW190512_180714', 'GW190630_185205', 'GW190513_205428']
list_O3b_events11  = ['GW191222_033537', 'GW200112_155838', 'GW191216_213338', 'GW191204_171526', 'GW191215_223052', 'GW200225_060421', 'GW200311_115853', 'GW200224_222234', 
                      'GW200129_065458', 'GW191129_134029', 'GW191109_010717']
list_all_SNR11     = ['GW150914', 'GW170814', 'GW170809', 'GW151226', 'GW170104', 'GW170818', 'GW170823', 'GW170608',
                      'GW190701_203306', 'GW190720_000836', 'GW190708_232457', 'GW190503_185404', 'GW190924_021846', 'GW190828_065509', 'GW190706_222641', 'GW190408_181802', 
                      'GW190915_235702', 'GW190728_064510', 'GW190727_060333', 'GW190707_093326', 'GW190828_063405', 'GW190602_175927', 'GW190521', 'GW190521_074359', 'GW190910_112807', 
                      'GW190519_153544', 'GW190412', 'GW190512_180714', 'GW190630_185205', 'GW190513_205428',
                      'GW191222_033537', 'GW200112_155838', 'GW191216_213338', 'GW191204_171526', 'GW191215_223052', 'GW200225_060421', 'GW200311_115853', 'GW200224_222234', 
                      'GW200129_065458', 'GW191129_134029', 'GW191109_010717']
# NSBH events
list_NSBH          = ['GW190814', 'GW200210'] 