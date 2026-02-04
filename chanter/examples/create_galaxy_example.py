import chanter as ch
import matplotlib.pyplot as plt

'''
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Define model galaxy parameters
'''

exp = {}
exp["age"] = 1                          # Age of galaxy in its rest frame
exp["tau"] = 0.3                        # Scale of star-formation exponential decline
exp["massformed"] = 11.                 # Total mass formed in stars
exp["metallicity"] = 0.02               # Z/Z_oldsolar

dust = {}
dust["type"] = "Calzetti"               # Type of dust law
dust["Av"] = 1                          # Dust extinction in magnitudes

fit_instructions = {}
fit_instructions["redshift"] = 5        # Redshift of galaxy
fit_instructions["exponential"] = exp
fit_instructions["dust"] = dust

'''
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
'''

# Plot CHANTER
model = ch.modelgalaxy(fit_instructions)
fig, ax = plt.subplots(figsize=(10, 3))
model.plot_spec(ax, dict(color='darkcyan'))
ax.set_xlim(1000, 50000)
fig, ax = plt.subplots(figsize=(10, 3))
model.plot_sfh(ax)
plt.show()












