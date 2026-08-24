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

data = pd.read_excel("meritve/data.ods", sheet_name="1", engine="odf")
print(data)

t = data.iloc[:,0].to_numpy()
x = data.iloc[:,1].to_numpy()
y = data.iloc[:,6].to_numpy()
x_err = data.iloc[:,2].to_numpy()
y_err = data.iloc[:,7].to_numpy()

cutoff = 0.20 # 8.5
mask = t <= cutoff
x = x[mask]
y = y[mask]
x_err = x_err[mask]
y_err = y_err[mask]

def lin_fit(x, k, n):
    return k * x + n

p0 = [1, 1]  # just k, n

popt, pcov = curve_fit(
    lin_fit, x, y,
    p0=p0,
    sigma=y_err if np.all(y_err > 0) else None,
    absolute_sigma=True,
    maxfev=10000
)

perr = np.sqrt(np.diag(pcov))

k_fit, n_fit = popt
k_err, n_err = perr

print(f"k = {k_fit:.4g} +/- {k_err:.2g}")
print(f"n = {n_fit:.4g} +/- {n_err:.2g}")

fig, ax = plt.subplots(figsize=(12, 8))

ax.errorbar(
    x, y,
    xerr=x_err,
    yerr=y_err,
    fmt='s',
    markersize=5,
    color='#1f3b73',
    ecolor='#444444',
    elinewidth=1,
    capsize=3,
    capthick=1,
    markeredgewidth=0.6,
    markeredgecolor='black',
    linestyle='none',
    label='Meritve: $U(\\omega)$'
)

ax.plot(
    x, lin_fit(x, k_fit, n_fit),
    color='#c0392b',
    linewidth=1.8,
    label=(
        rf'Fit: $k={k_fit:.4g}, k_e={k_err:.4g}$'
    )
)

ax.set_xlabel(r"$Em \,[C]$")
ax.set_ylabel(r"$e_{izracun} \,[C]$")
plt.legend()

plt.savefig("graf_umerjanja_zmanjsan.png", dpi=600)
plt.show()