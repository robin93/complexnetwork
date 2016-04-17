import pandas as pd
import json
from geopy.geocoders import GoogleV3
from geopy import geocoders
from time import sleep
import csv as csv
import os

cwd = os.getcwd()

with open('dandelion_by_municipality_api_large_limit.txt') as data_file:    
    raw_data = json.load(data_file)

print raw_data['items'][0]['parentNames']['province']
print raw_data['items'][0]['name']
print int(raw_data['items'][0]['population']['2001'])
g = geocoders.GoogleV3()

gcd = pd.read_csv(os.path.join(cwd,'Milano_GridGeoCoordinates.csv'),header = 0,sep = ",")
def AssignCoordinates(row):
	sleep(2)
	coordinates = g.geocode(row,timeout=10)
	if coordinates is not None:
		return [coordinates.longitude,coordinates.latitude]
		# print coordinates.longitude,coordinates.latitude
	else:
		return [0,0]

def CoordinatesToGrid(row1,row2):
	lat,lon = row1,row2
	subset = gcd[(gcd.longitude_small<lon)&(gcd.longitude_big>lon)&(gcd.latitude_small<lat)&(gcd.latitude_big>lat)]
	if len(subset)>0:
		return subset.iloc[0]['cellId']
	else:
		return 20000

municipality_count = 0
output_file = open("milano_grid_population_dandelion_api_401plus.txt", "w+")
for item in raw_data['items']:
	# print item['parentNames']
	if item['parentNames']['province'] == 'Milano':
		# print item['parentNames']
		# print "count",municipality_count,"name",item['name'],"population",item['population']['2001'],"grid",grid
		municipality_count += 1
		# print municipality_count
		if municipality_count > 401:
			# break
			coordinate_list = AssignCoordinates(item['name'])
			grid = CoordinatesToGrid(coordinate_list[1],coordinate_list[0])
			# print grid
			print "count",municipality_count,"name",item['name'],"population",item['population']['2001'],"grid",grid
			# print coordinate_list
			# # output_list = str([item['name'],item['population']['2001'],grid])
			# #output_list = "{0}\t{1}\t{2}".format(item['name'][0],item['population']['2001'],grid)
			if grid and grid != 20000:
				output_list = ((str(grid))+(",")+(str(item['population']['2001']))+("\n"))
				output_file.writelines(output_list)




