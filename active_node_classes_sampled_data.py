import pandas as pd
import numpy as np
import csv as csv
import os

cwd = os.getcwd()

data = pd.read_csv(os.path.join(cwd,'selected_timestamp_data_03_11_processed.csv'),header = 0,sep = ",",nrows=10000)

pivot = pd.pivot_table(data, values='Strenght_factor_scaled100000', index=['Timestamp_Number','Source'], columns=['Strenght_factor_ordinal'], aggfunc=lambda x: len(x.unique()),fill_value = 0)

# print pivot

def countfor1(row):
	if (row[1] > 0):
		return 1
	else:
		return 0

def countfor2(row):
	if (row[2] > 0):
		return 1
	else:
		return 0

def countfor3(row):
	if (row[3] > 0):
		return 1
	else:
		return 0

def countall(row):
	return 1

pivot['1_count'] = pivot.apply(countfor1,axis=1)
pivot['2_count'] = pivot.apply(countfor2,axis=1)
pivot['3_count'] = pivot.apply(countfor3,axis=1)
pivot['all_count'] = pivot.apply(countall,axis=1)

# print pivot

pivot.to_csv('timestamp_node_edge_classes_pivot.csv',sep = ',',index = True)

data = pd.read_csv(os.path.join(cwd,'timestamp_node_edge_classes_pivot.csv'),header = 0,sep = ",")

# print data

pivot = pd.pivot_table(data, values=['1_count','2_count','3_count','all_count'], index=['Timestamp_Number'], aggfunc= np.sum,fill_value = 0)


pivot.to_csv('timestamp_active_node_summary.csv',sep = ',',index = True)
