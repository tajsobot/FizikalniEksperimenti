import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd

plt.style.use('bmh')

filenames = ["meritve/ref.csv", "meritve/Gled.csv"]


#rdeca je ref
colors = ['#000000', '#d62728', '#2ca02c', '#ff7f0e', '#9467bd', '#8c564b']

fig, ax = plt.subplots(figsize=(10, 6))

for idx, filename in enumerate(filenames):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()

        header_idx = next(i for i, line in enumerate(lines) if "Index" in line and "X:" in line)
        df = pd.read_csv(filename,
                          skiprows=header_idx,
                          sep="\t",
                          decimal=",",
                          nrows=1368)

        x = df.iloc[:, 1].to_numpy()
        y = df.iloc[:, 2].to_numpy()

        color = colors[idx % len(colors)]
        ax.errorbar(
            x, y,
            yerr=0,
            xerr=0,
            fmt='o',
            markersize=2,
            color=color,
            ecolor='#444444',
            elinewidth=1,
            capsize=3,
            capthick=1,
            markeredgewidth=0.01,
            linestyle='none',
            label=filename.split('/')[-1]
        )

        print(f"✓ Loaded {filename}")

    except FileNotFoundError:
        print(f"✗ File not found: {filename}")
    except Exception as e:
        print(f"✗ Error loading {filename}: {e}")

plt.legend()
plt.xlabel(r"Wavelength (nm)")
plt.ylabel(r"Irradiance")
plt.tight_layout()
plt.show()