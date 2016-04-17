import pandas as pd
import csv as csv
import os

cwd = os.getcwd()
data = pd.read_csv(os.path.join(cwd,'selected_timestamp_data_03_11_processed.csv'),header=0,sep = ",")

print data.head(10)

subset = data[(data.Timestamp_Number == 85)&(data.Self_Edge_Indicator != 1)]
et expandtab ts=4 sw=4 ai
subset = subset.drop(['Self_Edge_Indicator','Strenght_factor_scaled100000'],1)
print subset.head(10)

level3_edgeNetwork = subset[(subset.Strenght_factor_ordinal == 3)]

print level3_edgeNetwork.head(20)

level3_edgeNetwork.csv('OneTimeStampLevel3.csv',sep = ',',index = False)
