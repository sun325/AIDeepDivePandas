# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#path = 'C:\\Users\\K\\AIDeepDiveMaterials\\' 
path = '//Users//Sundar//downloads//' # Replace with the folder containing the materials for this class
pd.__version__ 



df1 = pd.read_csv(path+'SPTSXComposite.csv', index_col='Ticker')
print(df1.shape)
df1.head()

df2 = pd.read_csv(path+'SPTSXCap_Employees.csv')
df2.head()

df3 = pd.read_csv(path+'SP_Transactions.csv')
df3.head()


#1)Create a DataFrame based on the guidance above. 
#Don't forget to drop duplicates from dataset 
#(b). Extra credit: Add a variable for the Total Value of Merger/Acquisition Transactions



#df1.describe
#df2.head()

#print(df1.shape)
#print(df2.shape)
#df3 = df1.join(df2, how='left', rsuffix='2') # Suffix must be supplied if columns of the same name exist in both
#print(df3.shape)
#print(df3.head())
#df3.head(3)


