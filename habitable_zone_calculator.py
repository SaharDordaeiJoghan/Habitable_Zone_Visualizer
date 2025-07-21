
# habitable_zone_calculator.py
# Author: Sahar Dordaei Joghan
# Date: September 2023
# Description:
#     This script visualizes the habitable zones (HZ) around stars of various spectral types (M, K, G, F, A).
#     Using the method of Kopparapu et al. (2013), it calculates conservative and optimistic HZ boundaries
#     in astronomical units (AU), then plots them horizontally to compare their extent around each star.

# =================== MIT License ===================
# Copyright (c) 2023 Sahar Dordaei Joghan
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software to use, modify, distribute, and publish with attribution.
# ===================================================

# ==== Import Required Libraries ====
import matplotlib.pyplot as plt
import numpy as np

# ==== Step 1: Define Stellar Types and Their Properties ====
spectral_types = ['M', 'K', 'G', 'F', 'A']
luminosities = [0.08, 0.45, 1.0, 2.5, 5.0]

# ==== Step 2: Define Function to Calculate HZ Boundaries ====
def calculate_hz_boundaries(luminosity):
    inner_conservative = np.sqrt(luminosity / 1.1)
    outer_conservative = np.sqrt(luminosity / 0.53)
    inner_optimistic = np.sqrt(luminosity / 1.78)
    outer_optimistic = np.sqrt(luminosity / 0.32)
    return inner_conservative, outer_conservative, inner_optimistic, outer_optimistic

# ==== Step 3: Compute Boundaries ====
conservative_bounds = []
optimistic_bounds = []

for L in luminosities:
    ic, oc, io, oo = calculate_hz_boundaries(L)
    conservative_bounds.append((ic, oc))
    optimistic_bounds.append((io, oo))

# ==== Step 4: Create Horizontal Plot ====
y = np.arange(len(spectral_types))
height = 0.3

plt.figure(figsize=(10, 6))

for i, (ic, oc) in enumerate(conservative_bounds):
    plt.barh(y[i] - height/2, oc - ic, left=ic, height=height,
             color='skyblue', edgecolor='black', label='Conservative HZ' if i == 0 else "")

for i, (io, oo) in enumerate(optimistic_bounds):
    plt.barh(y[i] + height/2, oo - io, left=io, height=height,
             color='lightgreen', edgecolor='black', label='Optimistic HZ' if i == 0 else "")

plt.xlabel('Distance from Star [AU]')
plt.ylabel('Spectral Type')
plt.title('Habitable Zone Boundaries by Spectral Type')
plt.yticks(y, [f"{stype}" for stype in spectral_types])
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('habitable_zone_comparison.png', dpi=300)
plt.close()
