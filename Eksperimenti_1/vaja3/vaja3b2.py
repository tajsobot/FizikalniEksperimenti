import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('3del.csv', delimiter='\t')  # Adjust delimiter if needed
data.columns = ['l', 'p', 'V', '1/V', 'p_err', 'V_err', '1/V_err']

# Perform linear regression on 1/V vs p
slope, intercept = np.polyfit(data['1/V'], data['p'], 1)  # Degree 1 for linear fit
k = slope  # Slope is the constant k in p = k * (1/V)

# Generate points for the fitted line
x_fit = np.linspace(min(data['1/V']), max(data['1/V']), 100)
y_fit = slope * x_fit + intercept

# Create the plot
plt.figure(figsize=(10, 6))
plt.errorbar(data['1/V'], data['p'], xerr=data['1/V_err'], yerr=data['p_err'],
             marker='o', linestyle='', color='b',  # Data points and line
             ecolor='black', elinewidth=0.5, capsize=3)  # Error bars

# Plot the linear fit
plt.plot(x_fit, y_fit, 'r--', label=f'fit: k = ({k:.2f})/V + {intercept:.2f}')

plt.title('p(1/V) with Linear Fit')
plt.xlabel('1/V [1/m^3]')
plt.ylabel('p [Pa]')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("2del3_with_fit.png", dpi=300)
plt.show()

# Print the slope (k)
print(f"The slope (k) is: {k:.2f} bar·cm^3")