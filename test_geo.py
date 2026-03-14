import plotly.graph_objects as go
import numpy as np

# Create grid of 100x50
lons = np.linspace(-180, 180, 100)
lats = np.linspace(-90, 90, 50)
lon_grid, lat_grid = np.meshgrid(lons, lats)
z = np.sin(np.deg2rad(lat_grid)) * np.cos(np.deg2rad(lon_grid))

fig = go.Figure(go.Scattergeo(
    lon=lon_grid.flatten(),
    lat=lat_grid.flatten(),
    marker=dict(
        color=z.flatten(),
        colorscale='RdBu_r',
        showscale=True,
        symbol='square',
        size=8
    )
))

fig.update_geos(
    projection_type="natural earth",
    showcoastlines=True, coastlinecolor="black",
    showcountries=True, countrycolor="black"
)

fig.write_html("test_geo.html")
