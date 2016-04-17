import pandas as pd
import numpy as np
import csv as csv
import os

cwd = os.getcwd()

print "Reading Data"
data = pd.read_csv(os.path.join(cwd,'selected_timestamp_data_03_11_processed.csv'),header = 0,sep = ",",nrows=100000)

print "Subsetting Data"
subset = data[data['Timestamp_Number']== 85]

print "Dropping Unnecessary Columns"
subset = subset.drop(['Timestamp_Number','Strenght_factor_scaled100000','Self_Edge_Indicator'],1)

def Reciprocal(row):
	if any((subset.Source == row['Destination']) & (subset.Destination== row['Source'])):
		return int(subset[(subset['Source']== row['Destination']) & (subset['Destination']== row['Source'])]['Strenght_factor_ordinal'])
	else:
		return 0

print "Calculating Reciprocal Row"
subset['Reciprocal'] = subset.apply(Reciprocal,axis=1)


print "Writing the output to csv"
subset.to_csv('reciprocity_output.csv',sep = ',',index = True)

print "Evaluating the pivot Table"
pivot = pd.pivot_table(subset, index=['Strenght_factor_ordinal','Reciprocal'],aggfunc=len,fill_value = 0)

print pivot

print "Writing pivot to csv"
pivot.to_csv('reciprocity_output_pivot.csv',sep = ',',index = True)


