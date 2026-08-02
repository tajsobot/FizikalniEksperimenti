import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

# Your 4 txt files
files = ["pojemek 1.txt"]

plt.figure(figsize=(10, 6))

for fname in files:
    # Load file while skipping header rows (first 6 lines in your example)
    df = pd.read_csv(fname, sep="\t", skiprows=7, decimal=",", names=["t","x","v","acc"])

    # Extract time (s) and position (m) – can change to velocity/acc if needed
    t = df["t"].to_numpy()
    x = df["v"].to_numpy()*-1

    # Scatter plot of raw data
    plt.scatter(t, x, s=15, alpha=0.7, label=f"{fname}"[:-6])

    coeffs, cov = np.polyfit(t, x, 1, cov=True)
    slope, intercept = coeffs
    slope_err = np.sqrt(cov[0, 0])  # standard error of slope

    fit_line = np.poly1d(coeffs)
    plt.plot(t, fit_line(t), linestyle="--", color="red",
             label=f"pojemek fit (k={slope:.3e} ± {slope_err:.1e})")


plt.xlabel("t(s)")
plt.ylabel("v(m/s)")
plt.title("v(t)")
plt.legend()
plt.grid(True)
ax = plt.gca()
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.5))  # ticks every 0.05 s
plt.tight_layout()
plt.savefig("pojemek.png",dpi=300)
plt.show()
