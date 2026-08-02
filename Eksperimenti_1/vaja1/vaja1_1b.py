import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

data = pd.read_csv('vaja1/vaja1TMT.csv', delimiter=';', decimal=',')
data.columns = ['time', 'force', 'position', 'velocity', 'acceleration']


plt.figure(figsize=(10, 6))
plt.plot(data['time'], data['position'], marker='o', linestyle='-', color='b')

plt.title('y(t)')
plt.xlabel('t[s]')
plt.ylabel('y[m]')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(0.2))  # major ticks every 0.1s
plt.gca().xaxis.set_minor_locator(ticker.MultipleLocator(0.05)) # minor ticks every 0.02s

plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(0.05))  # major ticks every 0.1s

plt.xticks(rotation=45)

plt.xlim(0, 4)

plt.tight_layout()

plt.savefig("TMTb.png", dpi=300)
plt.show()
