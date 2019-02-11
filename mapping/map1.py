import folium
import pandas
df1 = pandas.read_csv("Volcanoes_USA.txt")
lat = list(df1["LAT"])
lon = list(df1["LON"])
ele = list(df1["ELEV"])
name = list(df1["NAME"])
map = folium.Map(location=[41.66,-91.53],zoom_start = 6,tiles = "Mapbox bright")
fg1 = folium.FeatureGroup(name="Volcanoes")
fg2 = folium.FeatureGroup(name="Population")
for latitude,longitude,elevation,names in zip(lat,lon,ele,name):
    #print(type(names))
    ele_str = str(elevation)
    color1 = "green"
    if elevation>2000.0 and elevation <=3000:
        color1 = "orange"
    if elevation > 3000:
        color1 = "red"

    #fg.add_child(folium.CircleMarker(location=[latitude,longitude],popup = str(elevation) + " m" ,icon=folium.Icon(color = color1)))
    popup1 = str(elevation) + " m, " + names
    #print(type(popup1))
    fg1.add_child(folium.CircleMarker(location=[latitude,longitude],popup = folium.Popup(popup1,parse_html = True),fill_color=color1,color = "grey",fill = True, fill_opacity = 0.7,radius = 7))
fg2.add_child(folium.GeoJson(data = (open("world.json",'r',encoding = 'utf-8-sig').read()),
style_function = lambda x:{'fillColor':'green' if x['properties']['POP2005']<20000000
else 'orange' if 2000000<= x['properties']['POP2005']<1000000000 else 'red'}))

map.add_child(fg1)
map.add_child(fg2)
map.add_child(folium.LayerControl())
map.save("Map2.html")
