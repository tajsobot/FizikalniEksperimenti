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

data = pd.read_excel("meritve/data.ods", sheet_name="C3", engine="odf")
print(data)

x = data.iloc[:,0].to_numpy(); x = x * 2 * np.pi
y = data.iloc[:,1].to_numpy()
x_err = data.iloc[:,2].to_numpy(); x_err = x_err * 2 * np.pi
y_err = data.iloc[:,3].to_numpy()

def resonance_curve(w, U0, w0, Q):
    return U0 / np.sqrt(1 + (Q * (w / w0 - w0 / w))**2)

#zacetni ugibi
idx_max = np.argmax(y)
U0_guess = y[idx_max]
w0_guess = x[idx_max]

half_max = U0_guess / np.sqrt(2)
above = np.where(y >= half_max)[0]
if len(above) >= 2 and x[above[-1]] > x[above[0]]:
    fwhm_guess = x[above[-1]] - x[above[0]]
    Q_guess = w0_guess / fwhm_guess
else:
    Q_guess = 5.0  # fallback if the peak isn't well resolved

p0 = [U0_guess, w0_guess, Q_guess]

popt, pcov = curve_fit(
    resonance_curve, x, y,
    p0=p0,
    sigma=y_err if np.all(y_err > 0) else None,
    absolute_sigma=True,
    maxfev=10000
)
perr = np.sqrt(np.diag(pcov))

U0_fit, w0_fit, Q_fit = popt
U0_err, w0_err, Q_err = perr

f0_fit = w0_fit / (2 * np.pi)
f0_err = w0_err / (2 * np.pi)

print(f"U0 = {U0_fit:.4g} +/- {U0_err:.2g} V")
print(f"w0 = {w0_fit:.4g} +/- {w0_err:.2g} rad/s")
print(f"f0 = {f0_fit:.4g} +/- {f0_err:.2g} Hz")
print(f"Q  = {Q_fit:.4g} +/- {Q_err:.2g}")

# smooth curve for plotting the fit
w_fit = np.linspace(x.min(), x.max(), 2000)
y_fit = resonance_curve(w_fit, *popt)

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
    w_fit, y_fit,
    color='#c0392b',
    linewidth=1.8,
    label=(
        rf'Fit: $\omega_0={w0_fit:.4g}\,s^{{-1}}$, $\omega_e={w0_err:.2g}$, $Q={Q_fit:.3g}$'
    )
)

ax.set_xlabel(r"$\omega \,[s^{-1}]$")
ax.set_ylabel(r"$U\,[V]$")
plt.legend()

plt.savefig("graf_C3.png", dpi=600)
plt.show()