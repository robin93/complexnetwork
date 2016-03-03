import pandas as pd
import csv as csv
import os

cwd = os.getcwd()

timestamps_of_interest = [1.3834332E+12,1.3834512E+12,1.3834692E+12,1.3834752E+12,1.3834842E+12,1.3834992E+12,1.3835052E+12]
timestamp_number_dict = {1.3834332E+12:0,1.3834512E+12:30,1.3834692E+12:60,1.3834752E+12:70,1.3834842E+12:85,1.3834992E+12:110,1.3835052E+12:120}

selected_timestamp_data = pd.DataFrame(columns = ['Timestamp','Source','Destination','Edge_Strength','Self_Edge','Edge_strength_level'])

chunksize = 10**5
chunk_count = 0
df_index = 0
for data in (pd.read_csv(os.path.join(cwd,'selected_timestamp_data_03_11.csv'),header = None,sep = ",",chunksize = chunksize)):
	chunk_count += 1
	# if chunk_count == 10:
	# 	break
	print "chunknumber --- ", chunk_count
	data.columns = ['Timestamp','Source_GridLoc','Destination_GridLoc','Strenght_factor']
	for index,row in data.iterrows():
		timestamp = row['Timestamp']
		if timestamp in timestamps_of_interest:
			selected_timestamp_data.set_value(df_index,'Timestamp',timestamp_number_dict[timestamp])
			selected_timestamp_data.set_value(df_index,'Source',row['Source_GridLoc'])
			selected_timestamp_data.set_value(df_index,'Destination',row['Destination_GridLoc'])
			selected_timestamp_data.set_value(df_index,'Edge_Strength',row['Strenght_factor'])
			if (row['Source_GridLoc'] != row['Destination_GridLoc']):
				selected_timestamp_data.set_value(df_index,'Self_Edge',0)
			else:
				selected_timestamp_data.set_value(df_index,'Self_Edge',1)

			if (row['Strenght_factor']<4.9537572503600E-05):
				selected_timestamp_data.set_value(df_index,'Edge_strength_level',1)
			elif (row['Strenght_factor']>4.9537572503600E-05 and row['Strenght_factor'] < 0.000378677825463000):
				selected_timestamp_data.set_value(df_index,'Edge_strength_level',2)
			else:
				selected_timestamp_data.set_value(df_index,'Edge_strength_level',3)
			df_index += 1
					

#print selected_timestamp_data

edge_emergence_df.to_csv('selected_timestamp_add_columns_data_03_11.csv',sep = ',',index = False)


