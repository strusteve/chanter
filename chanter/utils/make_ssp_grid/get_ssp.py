import numpy as np
from astropy.table import Table
import pandas as pd
import matplotlib.pyplot as plt

def get_ssp(ascii_file):


    ages = pd.read_table(ascii_file, sep='\s+', nrows=1, header=None, dtype='float')
    ages = ages.to_numpy()[0][1:]
    ages_df = pd.DataFrame(ages, columns=['age'])

    waves = pd.read_table(ascii_file, sep='\s+', skiprows=6, nrows=1,  header=None, dtype='float')
    waves = waves.drop(waves.columns[0], axis=1)

    flux = pd.read_table(ascii_file, sep='\s+', skiprows=7, nrows=221, header=None)
    flux = flux.drop(flux.columns[0], axis=1)
    flux = flux.drop(flux.columns[-53:], axis=1)
    flux.columns = waves.to_numpy()[0]


    base = ages_df.join(flux)

    return base

specs = ['m22', 'm32', 'm42', 'm52', 'm62', 'm72', 'm82']


for spec in specs:
    df = get_ssp('ssp/ascii_files/bc2003_hr_xmiless_'+spec+'_chab_ssp.ised_ASCII')
    df.to_csv('ssp/'+spec+'_ssp.csv', index=False)

