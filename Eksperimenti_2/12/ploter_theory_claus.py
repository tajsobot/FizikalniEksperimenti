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

x = data.iloc[:,5].to_numpy()
y = data.iloc[:,4].to_numpy()
x_err = data.iloc[:,6].to_numpy()
y_err = data.iloc[:,7].to_numpy()

k_calc = -4886.94
n_calc = 13.13

def lin_fit(x, k, n):
    return k * x + n


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
    x, lin_fit(x, k_calc, n_calc),
    color='#c0392b',
    linewidth=1.8,
    label=(
        rf'Fit: $k={k_calc:.4g}, n={n_calc:.4g}$'
    )
)

ax.set_xlabel(r"$1/T \,[1/K]$")
ax.set_ylabel(r"$ln(p/p_0) \,[1]$")
plt.legend()

plt.savefig("graf_teoreticni.png", dpi=600)
plt.show()