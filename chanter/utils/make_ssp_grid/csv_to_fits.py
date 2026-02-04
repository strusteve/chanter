import numpy as np
from astropy.table import Table
import pandas as pd
import matplotlib.pyplot as plt
from astropy.io import fits


base22 = np.genfromtxt('ssp/m22_ssp.csv', delimiter=',')
base32 = np.genfromtxt('ssp/m32_ssp.csv', delimiter=',')
base42 = np.genfromtxt('ssp/m42_ssp.csv', delimiter=',')
base52 = np.genfromtxt('ssp/m52_ssp.csv', delimiter=',')
base62 = np.genfromtxt('ssp/m62_ssp.csv', delimiter=',')
base72 = np.genfromtxt('ssp/m72_ssp.csv', delimiter=',')
base82 = np.genfromtxt('ssp/m82_ssp.csv', delimiter=',')

master_base = np.array((base22, base32, base42, base52, base62, base72, base82))

hdul = fits.HDUList()
hdul.append(fits.PrimaryHDU())

for img in master_base:
    hdul.append(fits.ImageHDU(data=img))

hdul.writeto('ssp/ssps.fits')