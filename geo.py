import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt

from pipelines import get_database

db = get_database()
cities = db.injurygeo
residence = db.residencegeo

#### Get dataframes #####

cursor = cities.find()

cursor2 = residence.find()

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

df = pd.DataFrame(array, columns=["Counts", "City", "Longitude", "Latitude"])

res_array = []
for city in cursor2:
    res_array.append([city['count'], city['_id']])

for city in res_array:
    if city[0] is not None and city[1] is not None:
        cit, coord = city[1].split('\n')
        city[1] = cit
        Lat, Lon = coord.split(", ")
        Lat = Lat.replace("(", "")
        Lon = Lon.replace(")", "")
        city.append(float(Lon))
        city.append(float(Lat))
    else:
        res_array.remove(city)

res_df = pd.DataFrame(res_array, columns= ["Counts", "City", "Longitude", "Latitude"])

#### Conneticut map #####

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

ax.set_title('Injury Locations of Drug-related Deaths in CT')
plt.savefig("./plt/05_injurymap.png")

fig, ax = plt.subplots(figsize = (12,6))
connecticut_map.to_crs(epsg=4326).plot(ax=ax, color='lightgrey')
x2 = res_df['Longitude']
y2 = res_df['Latitude']
z2 = res_df['Counts']
plt.scatter(x2, y2, s=3*z2, c=z2, alpha=0.6,
            cmap='autumn_r')
plt.colorbar(label='Number Drug-related deaths')

ax.set_title('Residence of drug-related deaths in CT')
plt.savefig("./plt/06_residencemap.png")