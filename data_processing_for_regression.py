import csv as csv
import math

def InterGridDistance(source,destination):
	source_x,source_y,dest_x,dest_y = source%100,source//100,destination%100,destination//100
	return math.sqrt((math.pow((source_x-source_y),2)+math.pow((dest_x-dest_y),2)))

grid_pop_indicator_dict = dict()
count = 0
with open('all_grid_population_level_mapping2.txt','rU') as csvfile:
	spamreader = csv.reader(csvfile,delimiter='\t')
	for row in spamreader:
		count += 1
		if count > 1:
			grid_pop_indicator_dict[int(row[0])] = int(row[3])
print grid_pop_indicator_dict

output_file = open("regression_data3.txt", "w+")

row_count = 0
with open('one_timestamp_data_of8Nov_for_regression.txt','rU') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',')
	for row in spamreader:
		row_count += 1
		#if row_count > 1000:
		#	break
		print row_count
		source = int(row[0])
		destination = int(row[1])
		strength = float(row[2])*1000
		# print strength
		distance = InterGridDistance(source,destination)
		# print distance
		dist_square = math.pow(distance,2)
		dist_cube = math.pow(distance,3)
		core_core,core_peri,peri_core,peri_peri = "0","0","0","0"
		if ((source%100)>25 & (source%100)<75 & (source//100)>25 & (source//100)<75):
			if ((destination%100)>25 & (destination%100)<75 & (destination//100)>25 & (destination//100)<75):
				core_core = "1"
			else:
				core_peri = "1"
		else:
			if not ((destination%100)>25 & (destination%100)<75 & (destination//100)>25 & (destination//100)<75):
				peri_peri = "1"
			else:
				peri_core = "1"
		#print core_core,core_peri,peri_core,peri_peri

		source_pop = 0
		if source in grid_pop_indicator_dict.keys():
			source_pop = grid_pop_indicator_dict[source]

		dest_pop = 0
		if destination in grid_pop_indicator_dict.keys():
			dest_pop = grid_pop_indicator_dict[destination]


		HP_HP,HP_LP,LP_HP,LP_LP = "0","0","0","0"
		if (source_pop == 0):
			if (dest_pop==0):
				LP_LP = "1"
			else:
				LP_HP = "1"
		else:
			if (dest_pop==0):
				HP_LP = "1"
			else:
				HP_HP = "1"
		#print HP_HP,HP_LP,LP_HP,LP_LP

		# print [format(distance,'.2f'),format(dist_square,'.2f'),format(dist_cube,'.2f'),core_core,core_peri,peri_core,peri_peri,HP_HP,HP_LP,LP_HP,LP_LP,format(strength,'.2f')]
		output_list = ((format(distance,'.2f'))+(",")+(format(dist_square,'.2f'))+(",")+(format(dist_cube,'.2f'))+(",")+(core_core)+(",")+(core_peri)+(",")+(peri_core)+(",")+(peri_peri)+(",")+(HP_HP)+(",")+(HP_LP)+(",")+(LP_HP)+(",")+(LP_LP)+(",")+(format(strength,'.4f'))+("\n"))
		output_file.writelines(output_list)




