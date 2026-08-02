import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("bat.csv", delimiter="\t")
data = data[["I", "U", "I_err", "U_err"]]

# swap roles
X    = data["U"].to_numpy()      # now x = U
Y    = data["I"].to_numpy()      # now y = I
xerr = data["U_err"].to_numpy()
yerr = data["I_err"].to_numpy()

(coeffs, cov) = np.polyfit(
    X,
    Y,
    deg=1,
    w=1 / yerr,   # weight by y uncertainty (correct)
    cov=True
)

a, b = coeffs
a_err = np.sqrt(cov[0, 0])

X_fit = np.linspace(X.min(), X.max(), 300)
Y_fit = a * X_fit + b

plt.errorbar(
    X,
    Y,
    xerr=xerr,
    yerr=yerr,
    fmt='o',
    markersize=2,
    elinewidth=0.4,
    capsize=2,
    label="Data"
)

plt.plot(
    X_fit,
    Y_fit,
    "-",
    linewidth=0.5,
    label="Fit"
)

plt.xlabel("U [V]")
plt.ylabel("I [A]", rotation=0, labelpad=15)
plt.grid(True)
plt.legend()

plt.text(
    0.05,
    0.95,
    rf"$I = ({a:.2e} \pm {a_err:.2e})\,U + {b:.2e}$",
    transform=plt.gca().transAxes,
    verticalalignment="top"
)

plt.tight_layout()
plt.savefig("grafbat_inverted.png", dpi=300)
plt.show()
