import chanter as ch
import matplotlib.pyplot as plt
import numpy as np
from nautilus import Prior
import json

# Define the filter curve filepaths
filt_list = np.loadtxt('filters/filt_list.txt', dtype="str")

# Define the observed photometry (microJy), along with their errors.
phot_data = np.array(([ [0.00000114, 0.00000011],
                        [0.00281023, 0.00028102],
                        [0.03039540, 0.00303954],
                        [0.04083275, 0.00408327],
                        [0.06158577, 0.00615858],
                        [0.08333301, 0.00833330],
                        [0.15811047, 0.01581105],
                        [0.63260459, 0.06326046],
                        [0.96879516, 0.09687952],
                        [1.15809244, 0.11580924],
                        [1.30375688, 0.13037569] ]))

# Define the priors for each parameter
prior = Prior()
prior.add_parameter("age", dist=(0., 14.))
prior.add_parameter("tau", dist=(0.1, 15.))
prior.add_parameter("massformed", dist=(0, 13.))
prior.add_parameter("Av", dist=(0, 8.))
prior.add_parameter("redshift", dist=(0., 10.))

# Fit observed photometry
fitter = ch.galaxyfitter()
median_instructions, wavs, spectrum_samples, photometry_samples = fitter.fit(phot_data.copy(), prior, filt_list)

# Print the median galaxy parameters
print(json.dumps(median_instructions, sort_keys=True, indent=4))

# Define figure
fig, ax = plt.subplots()

# Plot the observed photometry
filt = ch.utils.filter_set(filt_list)
effwavs = filt.eff_wavs
phot_data_erg = phot_data.copy()
phot_data_erg.T[0] = 2.99792458E-05 * ((1e-6 * phot_data_erg.T[0]) / ((effwavs)**2))
phot_data_erg.T[1] = 2.99792458E-05 * ((1e-6 * phot_data_erg.T[1]) / ((effwavs)**2))
ax.errorbar(effwavs, phot_data_erg.T[0], phot_data_erg.T[1], ls='none', marker='D', capsize=3, color='xkcd:cherry', mec='black', mew=1, ecolor='black', zorder=5)

# Plot the fitted model
ax.plot(wavs,np.median(fitter.spectrum_samples, axis=0), color='darkcyan', alpha=0.5)
ax.scatter(effwavs,np.median(fitter.photometry_samples, axis=0), color='darkcyan', marker='D')
ax.set_xlim(100, 50000)
ax.set_ylim(0,)
ax.set_ylabel('Observed Flux / erg s$^{-1}$ cm$^{-2}$ Å$^{-1}$')
ax.set_xlabel('Observed Wavelength / Å')
plt.show()


