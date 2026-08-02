import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd

plt.style.use('bmh') #ZELO DOBER PRESET!!!

print(plt.style.available)

df = pd.read_excel("data1.ods", engine="odf")

print(df)
#PAZI!!! PRVA VRSTA SE NE UPOSTEVA !!!!
x = df.iloc[:,0].to_numpy()
y = df.iloc[:,1].to_numpy()
y_cal = df.iloc[:,5].to_numpy()
x_err = df.iloc[:,2].to_numpy()
y_err = df.iloc[:,3].to_numpy()

print(x); print(y); print(x_err); print(y_err)

# Model (linear fit)
def f(x, a, b):
    return a*x + b

# Fit
# params, cov = curve_fit(f, x, y, sigma=y_err)
# a, b = params
# errors = np.sqrt(np.diag(cov))

# Plot

#wow:
plt.errorbar(
    x, y,
    yerr=y_err,
    xerr=x_err,
    fmt='s',  # square markers
    markersize=4,  # smaller dots
    color='#1f3b73',  # dark blue (markers + line)
    ecolor='#444444',  # dark grey error bars
    elinewidth=1,  # thin error lines
    capsize=3,  # "T" caps size
    capthick=1,  # thickness of caps
    markeredgewidth=0.8,
    linestyle='none',  # no connecting lines
    label='meritve'
)
plt.errorbar(
    x, y_cal,
    yerr=0,
    xerr=0,
    fmt='s',  # square markers
    markersize=4,  # smaller dots
    color='#ff0000',  # dark red (markers + line)
    ecolor='#444444',  # dark grey error bars
    elinewidth=1,  # thin error lines
    capsize=3,  # "T" caps size
    capthick=1,  # thickness of caps
    markeredgewidth=0,
    linestyle='none',  # no connecting lines
    label='teorija'
)

x_fit = np.linspace(min(x), max(x), 100)
# plt.plot(x_fit, f(x_fit, a, b), label=f'fit: y={a:.2f}x+{b:.2f}')

plt.legend()
plt.xlabel(r"$\theta\,[^\circ]$")
plt.ylabel(r"$t_0\,[s]$")
plt.savefig("graf1.png", dpi=300)

plt.show()

# print("a =", a, "±", errors[0])
# print("b =", b, "±", errors[1])

#neke