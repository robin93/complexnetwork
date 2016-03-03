import pandas as pd
import csv as csv
import os

cwd = os.getcwd()

timestamps_of_interest = [1.38344E+12,1.38345E+12,1.38343E+12,1.38345E+12,1.38346E+12,1.38346E+12,1.38345E+12,1.38345E+12,1.38346E+12,1.38346E+12,1.38347E+12,1.38347E+12,1.38348E+12,1.38348E+12,1.38349E+12,1.38349E+12,1.3835E+12,1.3835E+12,1.38349E+12,1.38349E+12,1.38351E+12,1.38351E+12,1.38352E+12,1.38351E+12]
chunksize = 10**5
chunk_count = 0
for data in (pd.read_csv(os.path.join(cwd,'MItoMI-2013-11-03.txt'),header = None,sep = "\t",chunksize = chunksize)):
	chunk_count += 1
	print chunk_count
	if chunk_count == 1:
		selected_dataframe = data[data[0].isin(timestamps_of_interest)]
	else:
		subset = data[data[0].isin(timestamps_of_interest)]
		selected_dataframe = selected_dataframe.append(subset,ignore_index = True)	
	if chunk_count == 10:
		break

selected_dataframe.columns = ['Timestamp','Source_GridLoc','Destination_GridLoc','Strenght_factor']
selected_dataframe.to_csv('selected_timestamp_data_03_11_16timestamps.csv',sep = ',',index = False)