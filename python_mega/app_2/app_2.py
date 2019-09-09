import folium
import pandas

"""
HTML worldmap with markers.
"""

def get_color(elevation):
    if elevation < 1500:
        return "green"
    elif elevation >= 3000:
        return "red"
    else:
        return "orange"

data = pandas.read_csv("Volcanoes.txt")
lon = list(data['LON'])
lat = list(data['LAT'])
v_name = list(data['NAME'])
elev = list(data['ELEV'])

html = """<h4>Volcano information:</h4>
Name: %s
Height: %s m
"""

maps = folium.Map(
    location=[80, -100],
    zoom_start=6,
    tiles="Stamen Terrain"
    )

v_group = folium.FeatureGroup(name="Volcanoes")

for lt, ln, name, el in zip(lat, lon, v_name, elev):
    v_group.add_child(
        folium.CircleMarker(
            location=[lt, ln],
            popup=html % (name, str(el)),
            fill_color=get_color(el),
            color="grey"
            )
        )

p_group = folium.FeatureGroup(name="Population")

p_group.add_child(
    folium.GeoJson(
        data=open("world.json", 'r', encoding='utf-8-sig').read(),
        style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000 else 'red' if x['properties']['POP2005'] > 20000000 else 'orange'}
        )
    )

maps.add_child(v_group)
maps.add_child(p_group)

maps.add_child(folium.LayerControl())

maps.save("Map1.html")
