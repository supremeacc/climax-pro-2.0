# 🌍 ClimaScope — Interactive Climate Data Explorer

> Explore atmospheric datasets through interactive spatial and temporal visualization.

ClimaScope is a web-based dashboard that transforms raw NetCDF climate files into interactive maps, time-series graphs, and animations — making it easy to identify global patterns, regional anomalies, and temporal trends without writing a single line of code.

---

## Problem Statement

Climate datasets are large, multidimensional, and stored in formats like NetCDF that are difficult to explore visually. Researchers and students often need to write custom scripts just to inspect a single variable — slowing down analysis and making it harder to spot meaningful patterns.

## Solution

ClimaScope provides an interactive interface that allows users to:

- **Upload** any NetCDF climate dataset
- **Visualize** global spatial distributions on a world map
- **Analyze** time-series trends at any geographic location
- **Compare** climate variables across different time periods
- **Animate** how climate patterns evolve over time

---

## Key Features

### 🗺️ Global Spatial Visualization
Displays the spatial distribution of any climate variable on a Natural Earth projection with coastlines, country borders, and smooth color mapping.

### 📈 Temporal Analysis
Shows how a variable evolves over time at a selected location, with automatic resampling and trend smoothing.

### 🔄 Dataset Comparison
Compare two time points side-by-side to observe climate anomalies, with Gaussian-smoothed difference maps centered at zero.

### 🖱️ Interactive Map
Click anywhere on the map to select a location — the marker, coordinates, and time-series graph update instantly.

### 🎬 Animation Mode
Visualizes how climate patterns change across the full time dimension, with consistent color scaling across frames.

### 🔧 Adaptive Dataset Handling
Automatically detects variable types and units from metadata, applies conversions (K → °C, Pa → hPa), and selects appropriate color scales — no manual configuration needed.

---

## Technologies Used

| Technology | Purpose |
|---|---|
| **Python** | Core language |
| **Streamlit** | Dashboard framework |
| **Xarray** | NetCDF data handling |
| **NumPy** | Numerical operations |
| **Plotly** | Interactive visualizations |
| **SciPy** | Gaussian smoothing |

---

## Supported Dataset Format

**NetCDF (`.nc`)** with standard coordinate dimensions (`time`, `lat`/`latitude`, `lon`/`longitude`).

Typical climate variables supported:

- 🌡️ Temperature (air, sst, t2m)
- 🌊 Sea Level Pressure (slp, msl, prmsl)
- 💨 Wind Speed (uwnd, vwnd, u10, v10)
- 🌧️ Precipitation (precip, pr, tp)
- 🌊 Sea Surface Temperature (sst)

---

## How It Works

| Step | Action |
|---|---|
| **1** | Upload a NetCDF dataset via the sidebar |
| **2** | Select the variable and time range |
| **3** | Explore spatial distribution on the global map |
| **4** | Click a location or enter coordinates to analyze temporal trends |
| **5** | Compare different time periods or view animations |

---

## Example Datasets

Test with publicly available datasets:

- [NOAA/NCEP Reanalysis](https://psl.noaa.gov/data/gridded/data.ncep.reanalysis.html) — air temperature, sea level pressure, wind
- [NASA GISS Surface Temperature](https://data.giss.nasa.gov/gistemp/) — global temperature anomalies
- [NCEP/DOE Reanalysis 2](https://psl.noaa.gov/data/gridded/data.ncep.reanalysis2.html) — atmospheric variables

---

## Future Improvements

- 🌐 3D globe visualization
- 📊 Multi-variable overlay analysis
- 🤖 Predictive climate modeling
- ⚠️ Anomaly detection and alerting

---

## Running the Project

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

The dashboard will open at `http://localhost:8501`.

---

## Hackathon Context

This project was developed to demonstrate how interactive visualization tools can make complex climate datasets accessible to researchers, students, and decision-makers — without requiring programming expertise.

**Goal:** Provide an intuitive, adaptive interface for climate data exploration and analysis.
