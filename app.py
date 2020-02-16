import folium
import pandas
import io

data_json = io.open("population.json",'r',encoding='utf-8-sig').read()


data = pandas.read_csv("Volcanos.txt")
lon = list(data["LON"])
lat = list(data["LAT"])
elev = list(data["ELEV"])
location = list(data["LOCATION"])

def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 2500:
        return "orange"
    else:
        return "red"

map=folium.Map(location=[38.58, -99.09], zoom_start=6, titles="Stamen Terrain")

fg = folium.FeatureGroup(name="Volcanos")

for lt, ln, el, loc  in zip(lat,lon, elev, location):
    fg.add_child(folium.Marker(location=[lt, ln], popup=f"Elevation:{el} Location:{loc}", icon=folium.Icon(color=color_producer(el))))



fp = folium.FeatureGroup(name="Population")

fp.add_child(folium.GeoJson(data=data_json, style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))



map.add_child(fg)
map.add_child(fp)
map.add_child(folium.LayerControl())

map.save("Map1.html")

