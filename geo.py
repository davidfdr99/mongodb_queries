import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt

from pipelines import get_database

db = get_database()
cities = db.injurygeo

cursor = cities.aggregate([
    { "$sort": {'_id': 1}}
])

array = []
for city in cursor:
    array.append([city['count'], city['_id']])

for city in array:
    if city[0] is not None and city[1] is not None:
        cit, coord = city[1].split('\n')
        city[1] = cit
        Lat, Lon = coord.split(", ")
        Lat = Lat.replace("(", "")
        Lon = Lon.replace(")", "")
        city.append(float(Lon))
        city.append(float(Lat))
    else:
        array.remove(city)

df = pd.DataFrame(array[1:], columns=["Counts", "City", "Longitude", "Latitude"])

connecticut_map = gpd.read_file("shapes/tl_2019_09_cousub.shp")

# gdf = gpd.GeoDataFrame(df, geometry="Coords")

fig, ax = plt.subplots(figsize = (12,6))
connecticut_map.to_crs(epsg=4326).plot(ax=ax, color='lightgrey')

x = df['Longitude']
y = df['Latitude']
z = df['Counts']
plt.scatter(x, y, s=3*z, c=z, alpha=0.6,
            cmap='autumn_r')
plt.colorbar(label='Number Drug-related deaths')

ax.set_title('Injury Locations of Drug-related Deaths in Connecticut')
plt.show()