import pandas as pd
import numpy as np
import csv as csv
import os

cwd = os.getcwd()

print "Reading Data"
data = pd.read_csv(os.path.join(cwd,'reciprocity_output.csv'),header = 0,sep = ",",nrows=100)
print data.head()

print data['Reciprocal'].value_counts()

pivot = pd.pivot_table(data, index=['Strenght_factor_ordinal','Reciprocal'],aggfunc=len,fill_value = 0)

print pivot
