import sklearn
import numpy as np
from numpy import genfromtxt
from sklearn import linear_model
from sklearn.feature_selection import f_regression

#regr = linear_model.LinearRegression(normalize=False)
#raw_data = genfromtxt('regression_data_small.txt',delimiter=',')
#X_data,Y_values = raw_data[0:,1:11],raw_data[0:,11:]
#regr.fit(X_data,Y_values)
#print "regression coefficients",regr.coef_
#print "regression score ", regr.score(X_data,Y_values)


import statsmodels
from statsmodels.formula.api import ols
import pandas as pd

data = pd.read_csv('regression_data3.txt')
data.columns = ['Distance','SquareDistance','CubeDistance','Core_Core','Core_Peri','Peri_Core','Peri_Peri','Pop_High_High','Pop_High_Low','Pop_Low_High','Pop_Low_Low','Edge_Strength']
print data
cols_to_norm = ['Distance','SquareDistance','CubeDistance','Core_Core','Core_Peri','Peri_Core','Peri_Peri','Pop_High_High','Pop_High_Low','Pop_Low_High','Pop_Low_Low','Edge_Strength']
data[cols_to_norm] = data[cols_to_norm].apply(lambda x:(x-x.min()/(x.max()-x.min())))
model = ols('Edge_Strength~Distance+SquareDistance+CubeDistance+Core_Core+Core_Peri+Peri_Core+Peri_Peri+Pop_High_High+Pop_High_Low+Pop_Low_High+Pop_Low_Low',data).fit()
print model.summary()
