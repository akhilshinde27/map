import folium
import pandas
data=pandas.read_csv("Volcanoes.txt")
evl=list(data["ELEV"])
lat=list(data["LAT"])
lon=list(data["LON"])
def color_production(eval):
    if eval<1000:
        return "green"
    elif 2000<=eval<=3000:
        return "red"
    else:
        return "blue"
map=folium.Map(location=[43.0932589,-110.5987861],zoom_start=16)
fg=folium.FeatureGroup(name="mymap")
#dict={18.5774715:73.968964,18.5774715:73.968964,18.5771277:73.9691988,18.5771277:73.9691988}
for lt,ln,cl in zip(lat,lon,evl):
    fg.add_child(folium.CircleMarker(location=[lt,ln],radius=16,popup="Hotels",fill_color=color_production(cl),color="grey",fill_opacity=0.7))
fg.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
                            style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005']<10000000 else 'orange'
                                                     if 10000000<=x['properties']['POP2005']<20000000
                                                     else 'red'}))
map.add_child(fg)
map.save("maplocation.html")
