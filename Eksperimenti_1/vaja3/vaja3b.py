import pandas as pd
import matplotlib.pyplot as plt

# Adjust delimiter if needed
data = pd.read_csv('2del.csv', delimiter='\t')  # or ' ' if space-separated
data.columns = ['p', 'l', 'V', '1/V', 'p_err', 'V_err', '1/V_err']

plt.figure(figsize=(10, 6))
plt.errorbar(data['V'], data['p'], xerr=data['V_err'], yerr=data['p_err'],
             marker='o', linestyle='-', color='b',  # Main plot line and markers remain blue
             ecolor='black', elinewidth=0.5, capsize=3)  # Black, thinner error bars

plt.title('p(V)')
plt.xlabel('V [cm^3]')
plt.ylabel('p [bar]')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("2del2.png", dpi=300)
plt.show()
