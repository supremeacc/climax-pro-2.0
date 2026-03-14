import plotly.express as px
import plotly.graph_objects as go
import numpy as np

lons = np.linspace(-180, 180, 180)
lats = np.linspace(-90, 90, 90)
lon_grid, lat_grid = np.meshgrid(lons, lats)
z = np.sin(np.deg2rad(lat_grid)) * np.cos(np.deg2rad(lon_grid))

# Flatten the arrays
df = {
    'lon': lon_grid.flatten(),
    'lat': lat_grid.flatten(),
    'z': z.flatten()
}

fig = px.scatter_geo(
    df,
    lon='lon',
    lat='lat',
    color='z',
    projection="natural earth",
    color_continuous_scale="RdBu_r"
)
fig.update_traces(marker=dict(size=4, symbol='square'))
fig.update_layout(margin=dict(l=0,r=0,t=0,b=0))
fig.write_html("test.html")
