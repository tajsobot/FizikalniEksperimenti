import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
import matplotlib.font_manager as fm

plt.rcParams.update({
    'font.family': 'Arial',
    'font.size': 12,
    'axes.linewidth': 1.2,         # thicker frame
    'axes.edgecolor': 'black',
    'axes.labelsize': 13,
    'axes.labelweight': 'normal',
    'xtick.direction': 'in',       # ticks INSIDE the plot, like Origin
    'ytick.direction': 'in',
    'xtick.top': True,             # ticks on all four sides
    'ytick.right': True,
    'xtick.major.size': 6,
    'ytick.major.size': 6,
    'xtick.minor.size': 3,
    'ytick.minor.size': 3,
    'xtick.major.width': 1.2,
    'ytick.major.width': 1.2,
    'xtick.minor.visible': True,   # Origin shows minor ticks by default
    'ytick.minor.visible': True,
    'legend.frameon': True,
    'legend.edgecolor': 'black',
    'legend.fancybox': False,
    'figure.dpi': 120,
    'savefig.dpi': 300,
    'figure.figsize': (12, 8),
    #grid
    'axes.grid': True,
    'axes.grid.which': 'both',  # 'major', 'minor', or 'both'
    'axes.axisbelow': True,  # draw grid BEHIND data points, not on top
    'grid.color': '#b0b0b0',  # light grey, Origin-like
    'grid.linestyle': '-',  # solid lines (Origin default); try ':' for dotted
    'grid.linewidth': 0.3,
    'grid.alpha': 0.3,
})

data = pd.read_excel("meritve/data.ods", sheet_name="1_2", engine="odf")
print(data)

x = data.iloc[:,0].to_numpy()
y = data.iloc[:,8].to_numpy()
x_err = data.iloc[:,1].to_numpy()
y_err = data.iloc[:,9].to_numpy()

i_ref = 0  # index referencne meritve (izberi po zeljah)

theta_i, theta_i_err = y[i_ref], y_err[i_ref]
r_i, r_i_err = x[i_ref], x_err[i_ref]

# izloci referencno tocko iz podatkov za fit
mask = np.arange(len(x)) != i_ref
theta, theta_e = y[mask], y_err[mask]
r, r_e = x[mask], x_err[mask]

# razmerja
theta_ratio = theta / theta_i
r_ratio = r / r_i

# log10
log_theta_ratio = np.log10(theta_ratio)
log_r_ratio = np.log10(r_ratio)

#relativne napake
log_theta_err = (1/np.log(10)) * np.sqrt((theta_e/theta)**2 + (theta_i_err/theta_i)**2)
log_r_err = (1/np.log(10)) * np.sqrt((r_e/r)**2 + (r_i_err/r_i)**2)

def lin_fit_origin(x, n):
    return n * x

popt, pcov = curve_fit(
    lin_fit_origin, log_r_ratio, log_theta_ratio,
    sigma=log_theta_err, absolute_sigma=True, p0=[-2]
)
n_fit = popt[0]
n_err = np.sqrt(pcov[0,0])

print(f"n = {n_fit:.4g} +/- {n_err:.2g}")
print(f"odstopanje od -2: {(n_fit-(-2))/n_err:.2g} sigma")

fig, ax = plt.subplots(figsize=(12,8))
ax.errorbar(log_r_ratio, log_theta_ratio, xerr=log_r_err, yerr=log_theta_err,
            fmt='s', markersize=5, color='#1f3b73', ecolor='#444444',
            elinewidth=1, capsize=3, capthick=1, markeredgewidth=0.6,
            markeredgecolor='black', linestyle='none', label="Meritve")

xx = np.linspace(log_r_ratio.min(), log_r_ratio.max(), 100)
ax.plot(xx, lin_fit_origin(xx, n_fit), color='#c0392b', linewidth=1.8,
        label=rf'Fit: $n={n_fit:.3g} \pm {n_err:.2g}$')
ax.plot(xx, -2*xx, '--', color='green', linewidth=1.2, label=r'Teorija: $n=-2$')

ax.set_xlabel(r"$\log(r/r_i)$")
ax.set_ylabel(r"$\log(\vartheta'/\vartheta'_i)$")
plt.legend()
plt.savefig("graf_loglog2.png", dpi=600)
plt.show()