import pandas as pd
import numpy as np
import csv as csv
import os

cwd = os.getcwd()

def range_map(strength):
	if(strength >0 and strength <= 1.66334738904e-06):
		return 1.66334738904e-06
	elif(strength >1.66334738904e-06 and strength <= 2.63965745442e-06):
		return 2.63965745442e-06
	elif(strength >2.63965745442e-06 and strength <= 3.38744181685e-06):
		return 3.38744181685e-06
	elif(strength >3.38744181685e-06 and strength <= 9.02432370664e-06):
		return 9.02432370664e-06
	elif(strength >9.02432370664e-06 and strength <= 3.85876336334e-05):
		return 3.85876336334e-05
	elif(strength >3.85876336334e-05 and strength <= 4.95375725036e-05):
		return 4.95375725036e-05
	elif(strength >4.95375725036e-05 and strength <= 7.22991321748e-05):
		return 7.22991321748e-05
	elif(strength >7.22991321748e-05 and strength <= 8.77341287935e-05):
		return 8.77341287935e-05
	elif(strength >8.77341287935e-05 and strength <= 0.000151786047902):
		return 0.000151786047902
	elif(strength >0.000151786047902 and strength <= 0.000226858739318):
		return 0.000226858739318
	elif(strength >0.000226858739318 and strength <= 0.000378677825463):
		return 0.000378677825463
	elif(strength >0.000378677825463):
		return 0.00178575312921

chunksize = 10**5
chunk_count = 0
edge_strength_dist_dict = dict()
for data in (pd.read_csv(os.path.join(cwd,'MItoMI-2013-11-03.txt'),header = None,sep = "\t",chunksize = chunksize)):
	chunk_count += 1
	# if chunk_count == 10:
	# 	break
	print "chunknumber --- ", chunk_count
	data.columns = ['Timestamp','Source_GridLoc','Destination_GridLoc','Strenght_factor']
	for index,row in data.iterrows():
		# list_of_edge_strength.append(row['Strenght_factor'])
		range_maping = range_map(row['Strenght_factor'])
		if range_maping in edge_strength_dist_dict.keys():
				edge_strength_dist_dict[range_maping] = 1 + edge_strength_dist_dict[range_maping]
		else:
			edge_strength_dist_dict[range_maping] = 1

print edge_strength_dist_dict

print "Converting Dictionary to pandas dataframe"
edge_strength_dist_df = pd.DataFrame(columns = ['Strength_interval','Count'])
df_index = 0
for keys in edge_strength_dist_dict.keys():
	edge_strength_dist_df.set_value(df_index,'Strength_interval',keys)
	edge_strength_dist_df.set_value(df_index,'Count',edge_strength_dist_dict[keys])
	df_index += 1

print edge_strength_dist_df

print "Writing Dataframe to CSV"
edge_strength_dist_df.to_csv('Edge_strength_distribution_03_11.csv',sep = ',',index = False)



