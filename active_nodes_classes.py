 import pandas as pd
import csv as csv
import os

cwd = os.getcwd()

def strength_factor_level(strength_value):
	if (strength_value<4.9537572503600E-05):
		return 1
	elif(strength_value>4.9537572503600E-05 and strength_value<0.000378677825463000):
		return 2
	elif(strength_value>0.000378677825463000):
		return 3

timestamp_dict = dict()
chunksize = 10**2
chunk_count = 0
df_index = 0
for data in (pd.read_csv(os.path.join(cwd,'MItoMI-2013-11-03.txt'),header = None,sep = "\t",chunksize = chunksize)):
	chunk_count += 1
	if chunk_count == 10:
		break
	print "chunknumber --- ", chunk_count
	data.columns = ['Timestamp','Source_GridLoc','Destination_GridLoc','Strenght_factor']
	for index,row in data.iterrows():
		timestamp = (row['Timestamp'] - 1.3834332E+12)/600000
		if (row['Source_GridLoc'] != row['Destination_GridLoc']):
			if timestamp not in timestamp_dict.keys():
				timestamp_dict[timestamp] = dict()
			source_node = row['Source_GridLoc']
			if source_node not in timestamp_dict[timestamp].keys():
				timestamp_dict[timestamp][source_node] = [0,0,0]
			if (strength_factor_level(row['Strenght_factor']) == 1):
				timestamp_dict[timestamp][source_node][0] += 1
			elif (strength_factor_level(row['Strenght_factor']) == 2):
				timestamp_dict[timestamp][source_node][1] += 1
			elif (strength_factor_level(row['Strenght_factor']) == 3):
				timestamp_dict[timestamp][source_node][2] += 1

print timestamp_dict

# timestamp_node_edge_class_summary = pd.DataFrame.from_dict(timestamp_dict, orient='index', dtype=None)

# timestamp_node_edge_class_summary = pd.DataFrame(columns = ['Timestamp','Node','Level1_Edges','Level2_Edges','Level3_Edges'])

# print "Writing the dictionary to pandas dataframe"



# df_index = 0
# for timestamp in timestamp_dict.keys():
# 	#print "timestamp",timestamp
# 	print "df_index",df_index
# 	for source_node in timestamp_dict[timestamp].keys():
# 		timestamp_node_edge_class_summary.set_value(df_index,'Timestamp',timestamp)
# 		timestamp_node_edge_class_summary.set_value(df_index,'Node',source_node)
# 		timestamp_node_edge_class_summary.set_value(df_index,'Level1_Edges',timestamp_dict[timestamp][source_node][0])
# 		timestamp_node_edge_class_summary.set_value(df_index,'Level2_Edges',timestamp_dict[timestamp][source_node][1])
# 		timestamp_node_edge_class_summary.set_value(df_index,'Level3_Edges',timestamp_dict[timestamp][source_node][2])
# 		df_index += 1

# #print timestamp_node_edge_class_summary
# print "Writing the dataframe to csv file"
# timestamp_node_edge_class_summary.to_csv('timestamp_node_edge_class_summary_03_11.csv',sep = ',',index = False)

