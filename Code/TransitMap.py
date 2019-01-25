import gmplot
import pandas
from bs4 import BeautifulSoup
from shapely.geometry.polygon import Polygon
import math

apikey = "AIzaSyB9SbDxFzEubEN3icbAce4T2U262jskSlg"

# route = pandas.read_csv("../Data/Bus/Routes/route34.csv", sep=",")
buses = pandas.read_csv("../Data/Bus/Stats/Buses.csv", sep=",")
stops = pandas.read_csv("../Data/Bus/Stats/stops.csv", sep=",")
# routes = pandas.read_csv("../Data/Bus/Stats/routes.csv", sep=",")
# shapes = pandas.read_csv("../Data/Bus/Stats/shapes.csv", sep=",")
# bikes = pandas.read_csv("../Data/Bike_Data.csv", sep=",")
# gmap = gmplot.GoogleMapPlotter(35.050597, -85.250439, 12, apikey=apikey)
# print(route.dtypes)
# def map_stops(gmap):
#     latcoords = []  #  shape latitudes
#     longcoords = []  #  shape longitudes
#     coords = []  #  shape coordinates

    # Placing the shape coordinates into lists
    # for i, value in enumerate(route.values):
    #     # print(route.Latitude.values[i], route.Latitude.values[i+1] )
    #     latchange = math.fabs(route.Latitude.values[i] - route.Latitude.values[i+1])
    #     longchange = math.fabs(route.Longitude.values[i] - route.Longitude.values[i+1])
    #     if latchange < 0.01 and longchange < 0.01:
    #         coords.append(str(route.Latitude[i]) + "," + str(route.Longitude[i]))
    #         latcoords.append((route.Latitude[i]))
    #         longcoords.append((route.Longitude[i]))
    #     else:
    #         break
    # exit()
    # for i, value in enumerate(route.values):
    #     coords.append(str(route.Latitude[i]) + "," + str(route.Longitude[i]))
    #     latcoords.append((route.Latitude[i]))
    #     longcoords.append((route.Longitude[i]))

    # Placing all the weather station pins on the map, marked by cyan pin
    # for i, value in enumerate(latcoords[0:100]):
    #     gmap.marker(latcoords[i], longcoords[i], 'c')

    # gmap.plot(latcoords, longcoords, 'cornflowerblue', edge_width=5)
    # gmap.draw("../Visualization_Output/Chattanooga Route 34.html")
for i, info in enumerate(stops.values):
    for j, stuff in enumerate(buses.values):
        latDiff = math.fabs(stops.Latitude[i] - buses.Latitude[j])
        longDiff = math.fabs(stops.Longitude[i] - buses.Longitude[j])
        if latDiff >= 0.00004 and longDiff >= 0.00004:
            pass
        else:
            buses.stop_id.values[j] = stops.stop_id.values[i]
buses.to_csv('BusesWithStops.csv')

# map_stops(gmap)