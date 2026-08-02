import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("bat.csv", delimiter="\t")
data = data[["I", "U", "I_err", "U_err"]]

I    = data["I"].to_numpy()
U    = data["U"].to_numpy()
xerr = data["I_err"].to_numpy()
yerr = data["U_err"].to_numpy()

(coeffs, cov) = np.polyfit(
    I,
    U,
    deg=1,
    w=1 / yerr,
    cov=True
)

k, intercept = coeffs
k_err = np.sqrt(cov[0, 0])

I_fit = np.linspace(I.min(), I.max(), 300)
U_fit = k * I_fit + intercept

plt.errorbar(
    I,
    U,
    xerr=xerr,
    yerr=yerr,
    fmt='o',
    markersize=2,
    color="blue",
    elinewidth=0.4,
    capsize=2,
    label="Data"
)

plt.plot(
    I_fit,
    U_fit,
    "-",
    linewidth=0.5,
    color="red",
    label="Fit"
)

#labeli
plt.xlabel("I[A]")
plt.ylabel("U[V]",rotation=0, labelpad=15)
plt.grid(True)
plt.legend()

plt.text(
    0.05,
    0.95,
    rf"$k = {k:.2e} \pm {k_err:.2e}$",
    transform=plt.gca().transAxes,
    verticalalignment="top"
)

plt.tight_layout()
plt.savefig("grafbat.png", dpi=300)
plt.show()


