import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd

plt.style.use('bmh')

df = pd.read_csv("meritve/TajMeritve/Meritev2.csv", delimiter=";", decimal=",")

x = df.iloc[:,0].to_numpy()
y = df.iloc[:,1].to_numpy()

cutoff = 0.0
mask = x >= cutoff
x = x[mask] - cutoff
y = y[mask]

y = y / np.max(np.abs(y))

def f(t, omega, decay):
    return np.cos(omega*t) * np.exp(-decay*t)

# Fit
params, cov = curve_fit(f, x, y, p0=[10, 0.1])  # ← initial guesses
omega, decay = params
errors = np.sqrt(np.diag(cov))

# Plot
plt.errorbar(
    x, y,
    yerr=0, xerr=0,
    fmt='s',
    markersize=4,
    color='#1f3b73',
    ecolor='#444444',
    elinewidth=1,
    capsize=3,
    capthick=1,
    markeredgewidth=0,
    linestyle='none',
    label='meritve'
)

x_fit = np.linspace(min(x), max(x), 100)
y_fit = f(x_fit, omega, decay)
plt.plot(x_fit, y_fit,
         label=f'fit: $w$={omega:.3f}, $b$={decay:.3f}',
         linewidth=2)

plt.legend()
plt.xlabel(r"$t\,[s]$")
plt.ylabel(r"$x\,[m]$")
plt.savefig("graf1test.png", dpi=300, bbox_inches='tight')
plt.show()
print(f"ω = {omega:.4f} ± {errors[0]:.4f} rad/s")
print(f"b = {decay:.4f} ± {errors[1]:.4f} s⁻¹")