import numpy as np
import matplotlib.pyplot as plt

# Parametri
gamma = 1.4  # Adiabatni eksponent za zrak
k = 1000     # Konstanta (npr. v bar*cm^3^gamma)

# Podatki za graf
V = np.linspace(1, 10, 100)  # Prostornina od 1 do 10 cm^3
p = k / (V ** gamma)         # Tlak po adiabatni enačbi

# Skica
plt.figure(figsize=(8, 5))
plt.plot(V, p, 'r-', label=f'Adiabatna: $p = k/V^{{{gamma}}}$')
plt.title('Tlak v odvisnosti od prostornine (adiabatna sprememba)')
plt.xlabel('Prostornina $V$ [cm³]')
plt.ylabel('Tlak $p$ [bar]')
plt.grid(True, linestyle='--', linewidth=0.5)
plt.legend()
plt.tight_layout()
plt.show()