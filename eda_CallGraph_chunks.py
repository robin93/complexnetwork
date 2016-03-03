import pandas as pd
import csv as csv
import os

cwd = os.getcwd()

edge_emergence_dict = dict()

chunksize = 10**2
chunk_count = 0
for data in (pd.read_csv(os.path.join(cwd,'MItoMI-2013-11-03.txt'),header = None,sep = "\t",chunksize = chunksize)):
	chunk_count += 1
	if chunk_count == 10:
		break
	print "chunknumber --- ", chunk_count
	data.columns = ['Timestamp','Source_GridLoc','Destination_GridLoc','Strenght_factor']
	for index,row in data.iterrows():
		# print row
		timestamp = row['Timestamp']
		#print timestamp
		if (row['Source_GridLoc'] != row['Destination_GridLoc']):
			if timestamp in edge_emergence_dict.keys():
				edge_emergence_dict[timestamp] = row['Strenght_factor'] + edge_emergence_dict[timestamp]
				edge_emergence_dict[timestamp] = 1 + edge_emergence_dict[timestamp]
			else:
				edge_emergence_dict[timestamp] = row['Strenght_factor']
				

print "creation of timestamp and Aggregate_Strength dictionary complete"
# for keys in edge_emergence_dict.keys():
# 	print keys,edge_emergence_dict[keys]

first_timestamp = min(edge_emergence_dict.keys())
print 'first_timestamp',first_timestamp
edge_emergence_df = pd.DataFrame(columns = ['Timestamp_number','Timestamp','Aggregate_Strength'])


print "Converting Dictionary to pandas dataframe"
df_index = 0
for keys in edge_emergence_dict.keys():
	Timestamp_number = (keys - first_timestamp)/(10*60*1000)
	edge_emergence_df.set_value(df_index,'Timestamp',keys)
	edge_emergence_df.set_value(df_index,'Aggregate_Strength',edge_emergence_dict[keys])
	edge_emergence_df.set_value(df_index,'Timestamp_number',Timestamp_number)
	df_index += 1

print "Conversion to dataframe complete"

edge_emergence_df.to_csv('edge_emergence_df_03_11.csv',sep = ',',index = False)
