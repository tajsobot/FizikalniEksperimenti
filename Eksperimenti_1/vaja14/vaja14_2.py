import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('del2.csv', delimiter='\t')
data.columns = ['lnk', 'lnd']

# --- Pick only the first part of data for linear fit ---
n_points = 5  # change depending on where it's linear
x = data['lnd'][:n_points]
y = data['lnk'][:n_points]

# Linear regression
slope, intercept = np.polyfit(x, y, 1)
k = slope

# Generate line for plotting
x_fit = np.linspace(x.min(), x.max(), 200)
y_fit = slope * x_fit + intercept

# Plot
plt.scatter(x, y, label="Data", color="blue")
plt.plot(x_fit, y_fit, "--", color="red", label=f"Fit: y = {slope:.10f}x + {intercept:.3f}")
plt.xlabel("ln(d)")
plt.ylabel("ln(k)")
plt.title("Fit")
plt.legend()
plt.grid(True)

# Show k on the plot
plt.text(0.05, 0.95, f"k = {k:.11f}", transform=plt.gca().transAxes,
         fontsize=10, verticalalignment="top")
plt.savefig("graf2.png", dpi=300)
plt.show()
