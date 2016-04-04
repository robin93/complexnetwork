import pandas as pd
import csv as csv
import os

cwd = os.getcwd()

def assignGridType(grid_number,location_type):
	if location_type == 'Fashion':
		grid_typevalues_dict[grid_number][0] += 1
	elif location_type == 'Dining':
		grid_typevalues_dict[grid_number][1] += 1
	elif location_type == 'Finance':
		grid_typevalues_dict[grid_number][2] += 1
	elif location_type == 'Tourism':
		grid_typevalues_dict[grid_number][3] += 1
	elif location_type == 'Industry':
		grid_typevalues_dict[grid_number][4] += 1
	elif location_type == 'Residential':
		grid_typevalues_dict[grid_number][5] += 1

def GenerateNeighbours(centre_grid):
	fulllist = list()
	centrelineGridNumbers = list()
	for i in range(-3,4):
		if (centre_grid+i) > 0:
			centrelineGridNumbers.append(centre_grid+i)
	# return centrelineGridNumbers
	for grid in centrelineGridNumbers:
		for i in range(-3,4):
			if (grid + i*100)>0:
				fulllist.append(grid + i*100)
	fulllist.remove(centre_grid)
	return fulllist

grid_typevalues_dict = dict()
grid_typequalitative_dict = dict()
row_number = 0
with open('addressToGridNumber2.csv','rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in spamreader:
		if row_number != 0:
			phrase = row[len(row)-1]
			word_list = phrase.split(",")
			location_type = word_list[1]
			grid_number = int(float(word_list[len(word_list)-1]))
			if grid_number not in grid_typevalues_dict.keys():
				grid_typevalues_dict[grid_number] = [0,0,0,0,0,0]
				assignGridType(grid_number,location_type)
			else:
				assignGridType(grid_number,location_type)
		row_number += 1

print grid_typevalues_dict

primary_dict = grid_typevalues_dict.copy()

for centre_grid in primary_dict.keys():
	list_of_neighbours = GenerateNeighbours(centre_grid)
	for neighbours in list_of_neighbours:
		if neighbours not in grid_typevalues_dict.keys():
			grid_typevalues_dict[neighbours] = primary_dict[centre_grid]
		else:
			grid_typevalues_dict[neighbours] = [a+b for a,b in zip(grid_typevalues_dict[neighbours],primary_dict[centre_grid])]

print grid_typevalues_dict


grid_typevalues_df = pd.DataFrame(columns=['Grid','Fashion','Dining','Finance','Tourism','Industry','Residential'])
df_index = 0
for grid in grid_typevalues_dict.keys():
	grid_typevalues_df.set_value(df_index,'Grid',grid)
	columns = ['Fashion','Dining','Finance','Tourism','Industry','Residential']
	values = grid_typevalues_dict[grid]
	grid_typevalues_df.set_value(df_index,columns,values)
	df_index += 1

print grid_typevalues_df.head(20)
print grid_typevalues_df.tail(20)

grid_typevalues_df.to_csv('Grid_ActivityType_value.csv',sep = ',',index = False)









