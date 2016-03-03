import pandas as pd
import csv as csv
import os
cwd = os.getcwd()
timestamp_number_dict = {1.3834332E+12:0,1.3834512E+12:30,1.3834692E+12:60,1.3834752E+12:70,1.3834842E+12:85,1.3834992E+12:110,1.3835052E+12:120}

def timestamp_number_map(row):
	timestamp = row['Timestamp']
	timestamp_number = timestamp_number_dict[timestamp]
	return timestamp_number

def strength_factor_scaling(row):
	Strenght_factor = 1000000*row['Strenght_factor']
	return int(round(Strenght_factor,0))

def self_edge_indicator(row):
	if (row['Source'] == row['Destination']):
		return 1
	else:
		return 0

def strength_factor_level(row):
	strength = row['Strenght_factor']
	if (strength<4.9537572503600E-05):
		return 1
	elif(strength>4.9537572503600E-05 and strength<scp 0.000378677825463000):
		return 2
	elif(strength>0.000378677825463000):
		return 3

print "Beginning to read data"
data = pd.read_csv(os.path.join(cwd,'selected_timestamp_data_03_11.csv'),header = 0,sep = ",")#,nrows= 100)
print "Data is read"
data.columns = ['Timestamp','Source','Destination','Strenght_factor']

print 'Timestamp_Number calculation'
data['Timestamp_Number'] = data.apply(timestamp_number_map, axis=1)
print 'Strenght_factor_scaled100000 calculation'
data['Strenght_factor_scaled100000'] = data.apply(strength_factor_scaling, axis=1)
print "Self edge indicator calculation"
data['Self_Edge_Indicator'] = data.apply(self_edge_indicator, axis=1)
print "Strenght_factor_ordinal calculation"
data['Strenght_factor_ordinal'] = data.apply(strength_factor_level,axis=1)

print "Taking data subset"
sub_set = data[['Timestamp_Number','Source','Destination','Strenght_factor_scaled100000','Strenght_factor_ordinal','Self_Edge_Indicator']]

print "Writing data to CSV"

sub_set.to_csv('selected_timestamp_data_03_11_processed.csv',sep = ',',index = False)
print "Done"