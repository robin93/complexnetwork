import pandas as pd
import csv as csv
import os

cwd = os.getcwd()


def GenerateNeighbours(centre_grid):
	fulllist = list()
	centrelineGridNumbers = list()
	for i in range(-5,6):
		if (centre_grid+i*1) > 0:
			centrelineGridNumbers.append(centre_grid+i)
	for grid in centrelineGridNumbers:
		for j in range(-5,6):
			if (grid + j*100)>0:
				fulllist.append(grid + j*100)
	fulllist.remove(centre_grid)
	return fulllist

grid_typevalues_dict = dict()
grid_typequalitative_dict = dict()
row_number = 0
with open('Grid_population_primary_data.csv','rU') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',')
	for row in spamreader:
		if row_number != 0:
			grid_number = row[0]
			population_level = row[2]
			print grid_number
			print population_level
			if grid_number not in grid_typevalues_dict.keys():
				grid_typevalues_dict[grid_number] = [0,0]
				if population_level == "1":
					grid_typevalues_dict[grid_number][0] += 1
				else:
					grid_typevalues_dict[grid_number][1] += 1
		row_number += 1

# print grid_typevalues_dict

primary_dict = grid_typevalues_dict.copy()

for centre_grid in primary_dict.keys():
	list_of_neighbours = GenerateNeighbours(int(centre_grid))
	for neighbours in list_of_neighbours:
		if neighbours not in grid_typevalues_dict.keys():
			grid_typevalues_dict[neighbours] = primary_dict[centre_grid]
		else:
			grid_typevalues_dict[neighbours] = [a+b for a,b in zip(grid_typevalues_dict[neighbours],primary_dict[centre_grid])]

print grid_typevalues_dict

output_file = open("all_grid_population_level_mapping2.txt", "w+")
for key in grid_typevalues_dict.keys():
	output_list = ((str(key))+(",")+(str(grid_typevalues_dict[key][0]))+(",")+str(grid_typevalues_dict[key][1])+("\n"))
	output_file.writelines(output_list)




