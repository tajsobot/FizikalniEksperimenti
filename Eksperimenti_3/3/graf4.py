import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd

plt.style.use('bmh') #ZELO DOBER PRESET!!!

df = pd.read_excel("data4.ods", engine="odf")

print(df)
#PAZI!!! PRVA VRSTA SE NE UPOSTEVA !!!!
x = df.iloc[:,3].to_numpy() #T
y = df.iloc[:,0].to_numpy()
y2 = df.iloc[:,1].to_numpy()
# y_cal = df.iloc[:,5].to_numpy()
# x_err = df.iloc[:,2].to_numpy()
# y_err = df.iloc[:,3].to_numpy()

print(x); print(y);

# Model (linear fit)
def f(x, a, b):
    return a*x + b

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
    linestyle='-',  # no connecting lines
    label='naprej'
)
plt.errorbar(
    x, y2,
    yerr=0,
    xerr=0,
    fmt='s',  # square markers
    markersize=4,  # smaller dots
    color='#ff3b73',  # dark blue (markers + line)
    ecolor='#444444',  # dark grey error bars
    elinewidth=1,  # thin error lines
    capsize=3,  # "T" caps size
    capthick=1,  # thickness of caps
    markeredgewidth=0,
    linestyle='-',  # no connecting lines
    label='nazaj'
)

x_fit = np.linspace(min(x), max(x), 100)
# plt.plot(x_fit, f(x_fit, a, b), label=f'fit: y={a:.3e}x+{b:.3e}', linewidth=0.3)

plt.legend()
plt.xlabel(r"$T\,[K]$")
plt.ylabel(r"$U\,[V]$")

plt.savefig("graf4.png", dpi=300)


plt.show()

print("a =", a, "±", errors[0])
print("b =", b, "±", errors[1])

#neke

