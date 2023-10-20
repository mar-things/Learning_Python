import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt


df= pd.read_csv('MoviesData.csv',index_col=0,delimiter=',')
print("")
print(df)