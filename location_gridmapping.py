#code block to read the geojson file
# import json
# with open('milano-grid.geojson') as data_file:    
#     data = json.load(data_file)

import pandas as pd
import numpy as np
# GridGeoCoordinates = pd.DataFrame(columns= ['cellId','longitude_small','longitude_big','latitude_small','latitude_big'])

# grid_index = 0
# for grid in data['features']:
# 	print grid_index
# 	# if grid_index>3:
# 	# 	break
# 	GridGeoCoordinates.set_value(grid_index,'cellId',grid['properties']['cellId'])
# 	longitude_values,latitude_values = list(),list()
# 	for coordinates in grid['geometry']['coordinates'][0]:
# 		longitude_values.append(coordinates[0]),latitude_values.append(coordinates[1])
# 	columns = ['longitude_small','longitude_big','latitude_small','latitude_big']
# 	values = [np.min(longitude_values),np.max(longitude_values),np.min(latitude_values),np.max(latitude_values)]
# 	GridGeoCoordinates.set_value(grid_index,columns,values)
# 	grid_index += 1


# # print GridGeoCoordinates

# GridGeoCoordinates.to_csv('Milano_GridGeoCoordinates.csv',sep = ',',index = False)

# #code block to output lat-longitude for location addresses
# from geopy.geocoders import Nominatim
from geopy.geocoders import GoogleV3
from geopy import geocoders
from time import sleep
import csv as csv
import os

cwd = os.getcwd()

address_data = (pd.read_csv(os.path.join(cwd,'milano_address_list.csv'),header=0,sep = ",")).head(20)
# #gcd = grid_coordinates_data
gcd = pd.read_csv(os.path.join(cwd,'Milano_GridGeoCoordinates.csv'),header = 0,sep = ",")
# geolocator = Nominatim()
g = geocoders.GoogleV3()

# print address_data
def AssignCoordinates(row):
	sleep(1)
	coordinates = g.geocode(row['Address'],timeout=10)
	if coordinates is not None:
		return [coordinates.longitude,coordinates.latitude]
		print coordinates.longitude,coordinates.latitude
	else:
		return 0

def CoordinatesToGrid(row):
	lat,lon = row['latitude'],row['longitude']
	subset = gcd[(gcd.longitude_small<lon)&(gcd.longitude_big>lon)&(gcd.latitude_small<lat)&(gcd.latitude_big>lat)]
	if len(subset)>0:
		return subset.iloc[0]['cellId']
	else:
		return 20000	

address_data[['longitude','latitude']] = address_data.apply(AssignCoordinates,axis=1)
address_data['GridNumber'] = address_data.apply(CoordinatesToGrid,axis=1)

location_dict = dict()

print address_data
print gcd.head(10)

address_data.to_csv('addressToGridNumber.csv',sep = ',',index = False)