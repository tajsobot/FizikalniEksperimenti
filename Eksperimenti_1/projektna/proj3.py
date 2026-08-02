import os

import matplotlib.pyplot as plt
import numpy as np

# Data
V_cm3 = np.array([0.2,
                  1.3,
                  2.2,
                  2.8,
                  3.8,
                  ])
T_deg = np.array([ 30,
                   35,
                   40,
                   45,
                   50,
                   ])
T_Kel = T_deg + 273.15

V_m3 = (V_cm3 + 75 + 9) / 1000000

# Linearize by taking 1/V

y = V_m3
x = T_Kel

# Linear fit: p = a*(1/V) + b
coeffs = np.polyfit(x, y, 1)
fit_line = np.poly1d(coeffs)

# Plot
plt.figure(figsize=(8,5))
plt.plot(x, y, 'o', label='Meritve')
plt.plot(x, fit_line(x), '-', label=f'Fit: V = {coeffs[0]:.9f}(T) + {coeffs[1]:.9f}')

plt.xlabel('T[K]')
plt.ylabel('V[m^3]')
plt.title('Lineariziran graf V(T)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("graf3.png", dpi=300)
plt.show()
