import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd


df = pd.read_excel("data1.ods", engine="odf")

print(df)
#PAZI!!! PRVA VRSTA SE NE UPOSTEVA !!!!
x = df.iloc[:,2].to_numpy()
y = df.iloc[:,3].to_numpy()
# y_cal = df.iloc[:,5].to_numpy()
# x_err = df.iloc[:,2].to_numpy()
# y_err = df.iloc[:,3].to_numpy()

print(x); print(y);

# Model (linear fit)
def f(x, a, b):
    return a*x + b
x = x/3.11


# Fit
params, cov = curve_fit(f, x, y)
a, b = params
errors = np.sqrt(np.diag(cov))

# Plot

#wow:
plt.errorbar(
    x, y,
    yerr=0,
    xerr=0,
    fmt='s',  # square markers
    markersize=4,  # smaller dots
    color='#1f3b73',  # dark blue (markers + line)
    ecolor='#444444',  # dark grey error bars
    elinewidth=1,  # thin error lines
    capsize=3,  # "T" caps size
    capthick=1,  # thickness of caps
    markeredgewidth=0,
    linestyle='none',  # no connecting lines
    label='meritve'
)

plt.legend()
plt.xlabel(r"$t\,[s]$")
plt.ylabel(r"$x\,[m]$")
plt.savefig("graf1test.png", dpi=300)

plt.show()

print("a =", a)
print("b =", b)

#neke

