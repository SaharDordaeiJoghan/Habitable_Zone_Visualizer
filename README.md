# Habitable Zone Visualizer

A Python tool to visualize **habitable zones (HZ)** around main-sequence stars (M, K, G, F, A types). This script shows how both **conservative** and **optimistic** HZ ranges vary across spectral types using a horizontal bar chart.

---

## What It Does

- Uses accepted scientific data (Kopparapu et al. 2013, 2014) for both **conservative** and **optimistic** HZ boundaries.
- Plots a horizontal bar chart of the HZ range for five types of stars.
- Labels each bar with its spectral type (M to A).
- Saves a high-resolution plot as `habitable_zone_comparison.png`.

---

## Files Included

| File                           | Description                                               |
|--------------------------------|-----------------------------------------------------------|
| `habitable_zone_calculator.py` | Main Python script with full comments and citations       |
| `habitable_zone_comparison.png`| Output image comparing HZs across star types              |
| `README.md`                    | Project description and instructions                      |
| `LICENSE`                      | MIT License                                               |

---

## How to Run

1. **Install Dependencies**

Requires Python 3.10+ and the following packages:

```bash
pip install matplotlib numpy
```

2. **Run the Script**

```bash
python3 habitable_zone_calculator.py
```

3. **Output**

The image `habitable_zone_comparison.png` will be saved in your project folder.

---

## Scientific Notes

- The **Habitable Zone (HZ)** is defined as the region around a star where liquid water could exist on a planet’s surface.
- Two HZ models are shown:
  - **Conservative**: Based on stricter assumptions for Earth-like conditions.
  - **Optimistic**: Extends boundaries based on Venus/Mars historical conditions.
- Based on widely accepted models:
  - Kopparapu et al. (2013, 2014), with temperature classes taken from stellar models.

---

## Citation

Kopparapu, R. K., Ramirez, R., Kasting, J. F., et al. (2013).  
*Habitable Zones Around Main-sequence Stars: New Estimates*.  
The Astrophysical Journal, 765(2), 131.  
https://doi.org/10.1088/0004-637X/765/2/131

Kopparapu, R. K., Ramirez, R. M., SchottelKotte, J., et al. (2014).  
*Habitability of Planets Orbiting Cool Stars: Extending the Habitable Zone*.  
The Astrophysical Journal Letters, 787(2), L29.  
https://doi.org/10.1088/2041-8205/787/2/L29

---

## License

This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute with attribution.

---

## Author

**Sahar Dordaei Joghan**  
Created: September 2023  
Updated: July 2025 (for GitHub Portfolio) 

---

## Acknowledgments

- [NASA Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu/)
- [Astropy Project](https://www.astropy.org/)
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)
- [Event Horizon Telescope Collaboration](https://eventhorizontelescope.org/) *(inspired prior astrophysics projects)*  
- Special thanks to Kopparapu et al. (2013) for their foundational work on the habitable zone.
