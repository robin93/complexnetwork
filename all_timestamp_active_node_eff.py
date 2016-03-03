import pandas as pd
import numpy as np
import csv as csv
import os

cwd = os.getcwd()

def strength_factor_level(row):
	if (row['Strenght_factor']<4.9537572503600E-05):
		return 1
	elif(row['Strenght_factor']>4.9537572503600E-05 and row['Strenght_factor']<0.000378677825463000):
		return 2
	elif(row['Strenght_factor']>0.000378677825463000):
		return 3

def timestampNumber(row):
	value = (row['Timestamp']- 1.3834332E+12)/600000
	return value

timestamp_dict = dict()
chunksize = 10**2
chunk_count = 0
df_index = 0
for data in (pd.read_csv(os.path.join(cwd,'MItoMI-2013-11-03.txt'),header = None,sep = "\t",chunksize = chunksize)):
	chunk_count += 1
	if chunk_count == 100:
		break
	print "chunknumber --- ", chunk_count
	if chunk_count == 1:
		data.columns = ['Timestamp','Source_GridLoc','Destination_GridLoc','Strenght_factor']
		data = data.drop('Destination_GridLoc',1)
		data['Timestamp'] = data.apply(timestampNumber,axis=1)
		data['Strenght_factor'] = data.apply(strength_factor_level,axis=1)
		data = data.drop_duplicates()
		aggregate_dataset = data
		print data
	else:
		data.columns = ['Timestamp','Source_GridLoc','Destination_GridLoc','Strenght_factor']
		data = data.drop('Destination_GridLoc',1)
		data['Timestamp'] = data.apply(timestampNumber,axis=1)
		data['Strenght_factor'] = data.apply(strength_factor_level,axis=1)
		data = data.drop_duplicates()
		aggregate_dataset = aggregate_dataset.append(data,ignore_index = True)
		aggregate_dataset = aggregate_dataset.drop_duplicates()
		print data

print aggregate_dataset

pivot = pd.pivot_table(aggregate_dataset, values='Source_GridLoc', index='Timestamp',columns='Strenght_factor',aggfunc=lambda x: len(x.unique()),fill_value = 0)

pivot.to_csv('all_timestamp_activenode_summary_new.csv',sep = ',',index = True)


