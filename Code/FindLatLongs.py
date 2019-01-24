import requests
import pandas
import numpy as np
import requests
from bs4 import BeautifulSoup

apikey = "AIzaSyB9SbDxFzEubEN3icbAce4T2U262jskSlg"

# bikes = pandas.read_csv("../Data/BikeStations.csv", sep=",")
# print(bikes.columns.values)

# cars = pandas.read_csv("../Data/GreenCommuterStations.csv", sep=",")
# print(cars.columns.values)

trips = pandas.read_csv("../Data/Bus/Stats/trips.csv", sep=",")
shapes = pandas.read_csv("../Data/Bus/Stats/shapes.csv", sep=",")

buses = trips.merge(shapes, on='shape_id')
print(buses.columns.values)

buses.to_csv('../Data/Bus/Stats/Buses.csv')
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} # This is chrome, you can set whatever browser you like


# page = requests.get("https://bikechattanooga.com/system-map/", headers=headers)
# soup = BeautifulSoup(page.text, features='html.parser')#make soup that is parse-able by bs
# # tbl = soup.find('div') 
# what = soup.find(id='infoWind')

# maybe = soup.find_all(class_='infoAdd')
# # print(type(maybe))
# stations = []
# for child in maybe:
#     # print(child.text)
#     stations.append(child.text)
# print(stations)
# stations = pandas.DataFrame({'Station':stations})
# stations.to_csv('BikeStations.csv')

# maybe = what.children
# print(type(maybe))
# print(maybe)
# for litag in maybe:
#     # print(litag, "This is the type of the thing:",type(litag), litag.name)
#     for station in litag:
#         try:
#             if ['infoAdd'] in station.attrs:
#                 print(station, type(station), station.attrs)
#         except: 
#             pass
#         print('Space')
        # if type(station) is 'bs4.element.Tag':
        # print(station, "This is the type of the thing:",type(station))
        # for info in station: 
        #     print(info)
            # for thing in info: 
            #     if isinstance(thing, str):
            #         print(thing)
exit()
# webaddress = str("https://maps.googleapis.com/maps/api/geocode/json?address="+(bikes.Station[40])+", Chattanooga, TN"+"&key="+apikey)
# print(webaddress)
# print(bikes.columns.values)
# print(bikes.Station.values[0])
# start = bikes.Start_Station_Name.unique()
# end = bikes.End_Station_Name.unique()

# stations = np.concatenate((start, end), axis=0)
# stations = list(stations)
# stations = np.unique(stations)

# print(stations)
# stations = pandas.DataFrame({'Station':stations})
# stations.to_csv('BikeStations.csv')

# print(bikes.values[0])

for i,info in enumerate(bikes.values):
    print(i)
    # print(bikes.Station.values[i])
    # exit()
    webaddress = str("https://maps.googleapis.com/maps/api/geocode/json?address="+(bikes.Station[i])+", Chattanooga&key="+apikey)
    try:
        response = requests.get(webaddress)

        resp_json_payload = response.json()
        # print(resp_json_payload['results', 'address_components'])
        # exit()
        # if('Chattanooga' in resp_json_payload['results','address_components']):
        print(resp_json_payload['results'][0]['geometry']['location'])
    except: 
        # print("Whoops.")
        pass