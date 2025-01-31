import pandas as pd

# "C:\Users\amineeva\OneDrive - Olin College of Engineering\2024-2025\Semester 2\Astro\hlsp_k2sff_k2_lightcurve_210312947-c04_kepler_v1_llc-default-aper.txt"

df = pd.read_fwf('hlsp_k2sff_k2_lightcurve_210312947-c04_kepler_v1_llc-default-aper.txt')
df.to_csv('hlsp_k2sff_k2_lightcurve_210312947-c04_kepler_v1_llc-default-aper.csv')