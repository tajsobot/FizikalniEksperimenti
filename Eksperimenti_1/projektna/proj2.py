import os

import matplotlib.pyplot as plt
import numpy as np

# Data
dP_Pa = np.array([568.98,
                  1000.62,
                  1549.98,
                  1824.66,
                  2118.96,
                  ])
T_deg = np.array([30,
                  35,
                  40,
                  45,
                  50,
                  ])

P_Pa = dP_Pa + 101400
T_Kel = T_deg + 273.15

# Linearize by taking 1/V

x = T_Kel
y = P_Pa

# Linear fit: p = a*(1/V) + b
coeffs = np.polyfit(x, y, 1)
fit_line = np.poly1d(coeffs)

# Plot
plt.figure(figsize=(8, 5))
plt.plot(x, y, 'o', label='Data')
plt.plot(x, fit_line(x), '-', label=f'Fit: p = {coeffs[0]:.2f}(T) + {coeffs[1]:.2f}')

plt.xlabel('T[K]')
plt.ylabel('P[Pa]')
plt.title('Lineariziran graf P(T)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("graf2.png", dpi=300)
plt.show()
