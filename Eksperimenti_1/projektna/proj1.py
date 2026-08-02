import os

import matplotlib.pyplot as plt
import numpy as np

# Data
pressure_kPa = np.array([99.58,
                         105.3,
                         113.75,
                         123.85,
                         135.4,
                         150,
                         168.8,
                         190.6,
                         ])
volume_cm3 = np.array([50,
                       45,
                       40,
                       35,
                       30,
                       25,
                       20,
                       15,
                       ])

# Linearize by taking 1/V
inv_volume = 1 / ((volume_cm3 + 9)/1000000)
pressure_Pa = pressure_kPa * 1000

x = inv_volume
y = pressure_Pa

# Linear fit: p = a*(1/V) + b
coeffs = np.polyfit(x, y, 1)
fit_line = np.poly1d(coeffs)

# Plot
plt.figure(figsize=(8,5))
plt.plot(x, y, 'o', label='Meritve')
plt.plot(x, fit_line(x), '-', label=f'Fit: p = {coeffs[0]:.2f}(1/V) + {coeffs[1]:.2f}')

plt.xlabel('1/V [1/m³]')
plt.ylabel('p[Pa]')
plt.title('Lineariziran graf P(1/V)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("graf1.png", dpi=300)
plt.show()
