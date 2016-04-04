import pandas as pd
import numpy as np
import networkx as nx
import six
import matplotlib.pyplot as plt
import csv as csv
import os

cwd = os.getcwd()

print "Reading Data"
data = pd.read_csv(os.path.join(cwd,'selected_timestamp_data_03_11_processed.csv'),header = 0,sep = ",",nrows=100)

print "Subsetting Data"
subset = data[data['Timestamp_Number']== 85]

print "Dropping Unnecessary Columns"
subset = subset.drop(['Timestamp_Number','Strenght_factor_scaled100000','Self_Edge_Indicator'],1)

print subset

G=nx.from_pandas_dataframe(subset,'Source','Destination','Strenght_factor_ordinal')

print sorted(nx.degree(G).values())

print nx.degree(G)

nx.draw(G)
plt.show()