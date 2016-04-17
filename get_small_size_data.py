import pandas as pd
import os,csv

def strength_level_map(row):
	s_value = row['Edge_strength']
	if s_value < 4.9537572503600E-05:
		return 1
	elif (s_value > 4.9537572503600E-05 and s_value < 0.00378677825463000):
		return 2
	else:
		return 3 

cwd = os.getcwd()
data = pd.read_csv(os.path.join(cwd,'MItoMI-2013-11-03.txt'),header=None,sep="\t",nrows=100000)
data.columns = ['Timestamp','Source','Destination','Edge_strength']
data['Edge_Strength_level'] = data.apply(strength_level_map,axis=1)

data['Timestamp_number'] = (data['Timestamp'] - 1.3834332E+12)/60000

print data.head(10)

data.to_csv('small_dataset_3Nov.csv',sep=',',index=False)
