import gmplot
import pandas
from bs4 import BeautifulSoup

apikey = "AIzaSyB9SbDxFzEubEN3icbAce4T2U262jskSlg"


stops = pandas.read_csv("../Data/Bus/Stats/stops.csv", sep=",")
gmap = gmplot.GoogleMapPlotter(35.050597, -85.250439, 12, apikey=apikey)
latcoords = []  # Weather station latitudes
longcoords = []  # Weather station longitudes
coords = []  # Weather station coordinates

# Placing the weather station coordinates into lists
for i, value in enumerate(stops.values):
    coords.append(str(stops.stop_lat[i]) + "," + str(stops.stop_lon[i]))
    latcoords.append((stops.stop_lat[i]))
    longcoords.append((stops.stop_lon[i]))

# Placing all the weather station pins on the map, marked by cyan pin
for i, value in enumerate(latcoords[0:len(latcoords)]):
    gmap.marker(latcoords[i], longcoords[i], 'c', title=stops.stop_name.values[i])

gmap.draw("../Visualization_Output/Chattanooga Bus Stations.html")