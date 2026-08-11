import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import pandas as pd
from pathlib import Path

plt.style.use('bmh')

results = []

for i in range(1, 16):
    filepath = f"meritve/taj2-{i}.csv"

    if not Path(filepath).exists():
        print(f"not found: {filepath}")
        continue

    try:
        df = pd.read_csv(filepath, delimiter=";", decimal=",")
        x = df.iloc[:,0].to_numpy()
        y = df.iloc[:,1].to_numpy()

        pre_cutoff = 0.
        mask = x >= pre_cutoff
        x = x[mask] - pre_cutoff
        y = y[mask]

        cutoff = 400
        mask = x <= cutoff
        x = x[mask]
        y = y[mask]

        #najde maximume in razdalje med njimi
        amplitude = (np.max(y) - np.min(y)) / 2
        peaks, _ = find_peaks(y)

        sample_peaks = 7
        t_peak1 = x[peaks[0]]
        t_peak2 = x[peaks[sample_peaks -1]]
        period = (t_peak2 - t_peak1)/sample_peaks
        frequency = 1 / period  # w = 2 pi /T

        results.append({
            'file': f'taj2-{i}',
            'amplitude': amplitude,
            'frequency_hz': frequency,
        })

        # Plot
        plt.figure(figsize=(12, 6))
        plt.plot(x, y, 's', markersize=4, color='#1f3b73', label='Data', alpha=0.7)
        plt.plot(x[peaks], y[peaks], 'ro', markersize=8, label=f'Peaks (T = {period:.4f} s)')

        plt.xlabel(r"$t$ [s]", fontsize=12)
        plt.ylabel(r"$x$ [m]", fontsize=12)
        plt.title(f"taj2-{i} | A = {amplitude:.4f} m, ω = {frequency:.4f} rad/s", fontsize=14)
        plt.legend(fontsize=11)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"✗ taj2-{i}: Error - {e}")

if results:
    results_df = pd.DataFrame(results)
    results_df.to_csv("fit_data.csv", index=False)

    #koncni plot
    plt.figure(figsize=(10, 6))
    plt.plot(results_df['frequency_hz'], results_df['amplitude'],
             'o', markersize=8, linewidth=2, color='#1f3b73')

    plt.xlabel(r"Frekvenca $v$ [hz]", fontsize=12)
    plt.ylabel(r"Amplituda $A$ [m]", fontsize=12)
    plt.title("Resonančna krivulja", fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()