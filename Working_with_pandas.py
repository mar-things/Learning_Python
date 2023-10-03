import numpy as np
import pandas as pd
import json
import matplotlib.pyplot as plt


# Series - it is vasicaly column, one dimensional 
# DataFrames - colection of Series or columns, multidimensional
#
#Creating DataFrame from dict variable
data = {'apples':[3,2,0,1],'oranges':[0,3,7,2]}

print (data)


purchase = pd.DataFrame(data)
print (purchase)

#making custom indexing in DataFrames
purchase = pd.DataFrame(data, index=['Kestas', 'Uladislau', 'Emma', 'Rita'])
print (purchase)

#Locating data that correspond to certain person
print('')

print(purchase.loc['Uladislau'])

#Loading data from CSV file 

df= pd.read_csv('Data.csv',index_col=0,delimiter=',')
print("")
print(df)


#loading data in JSON format

#with open('Data.json', 'w') as file:
#    json.dump(data,file)
    

df2= pd.read_json('Data.json')
print("")
print(df2)

# Saving data to different formats using pandas

df.to_csv('new_data.csv')
df.to_json('new data.json')

#---------- Operations with data frames--------------

mov_df = pd.read_csv('MoviesData.csv')
print(mov_df)

#head() to limit list rows
print(mov_df.head())
print(mov_df.head(10))

#tail() to limit list rows to the end

print("")
print(mov_df.tail())

#get information about dataframe
#number of colums, rows, how much memory is used non-null values ....
print(mov_df.info())

print(mov_df.shape)


#handling a duplicates
temp_df = mov_df._append(mov_df)
print(temp_df.shape)

#temp_df = temp_df.drop_duplicates()
#print(temp_df.shape)

temp_df.drop_duplicates(inplace=True)
print(temp_df.shape)

#Other options to remove duplicates 
#first: (Default)except first one
#last: except last one
#False: Remove all duplicates

temp_df = mov_df._append(mov_df)
print(temp_df.shape)
temp_df.drop_duplicates(inplace=True,keep=False)
print(temp_df.shape)

#printing the names of columns
print(mov_df.columns)
mov_df.rename(columns={'Runtime (Minutes)':'Runtime',
                       'Revenue (Millions)':'Revenue_Millions'},inplace=True)
print(mov_df.columns)

#mov_df.columns = ['rank', 'title', 'genre', 'description', 'director', 'actors', 'year',
#       'runtime', 'rating', 'votes', 'revenue_millions', 'metascore']
#print(mov_df.columns)

mov_df.columns =[col.lower() for col in mov_df]
print(mov_df.columns)

#---- 1. Removing NaN values in the data
#---- 2. changing it to otehr values (IMPUTATION)
print(mov_df.isnull())
print(mov_df.isnull().sum())

#remove not values (NaN/Null)
mov_df2 = mov_df.dropna()
print(mov_df2.isnull().sum())

#removing columns with NaN/Null values
mov_df2 = mov_df.dropna(axis=1)
print(mov_df2.isnull().sum())

#Imputation
revenue = mov_df['revenue_millions']
print(revenue)
print(revenue.head(5))
revenue_mean = revenue.mean()
print(revenue_mean)

#Replacing 
revenue.fillna(revenue_mean,inplace=True)
print(revenue.head(10))





metascore = mov_df['metascore']
metascore_mean = metascore.mean()
print(metascore_mean)
#replacing
metascore.fillna(metascore_mean,inplace=True)
#checking again the NaN values
print(mov_df2.isnull().sum())




# ---- Calculating statistical values in data frame (.describe())
print(mov_df.describe())
# based on category (specific column)
print(mov_df['genre'].describe())
# frequency of appearance based on genre
print(mov_df['genre'].value_counts().head(10))

#Calculation correlations between numberical values in dataframe
print("")
print(mov_df.corr(numeric_only=True))

#Slice the dataframe

genre_col = mov_df['genre']
print(type(genre_col))
genre_col = mov_df[['genre','rating']]
print(type(genre_col))


#.lco - locates by name 
#.iloc - locatesby index 
print("")
prom = mov_df.loc['Prometheus']
print("")
#print(prom)

prom = mov_df.iloc[1]
print("")
print(prom)

slice_of_data = mov_df.loc['Prometheus':'Sing']
print("")
print(slice_of_data)
sile_of_data =mov_df.iloc[1:4]
print(sile_of_data)

# ---- Selecting data based on conditions
cond = (mov_df['director']=='Ridley Scott')
print(cond)
print(mov_df[mov_df['director']=='Ridley Scott'])

#filter out movies with rating above 8.6
print(mov_df[mov_df['rating'] >= 8.6].head(3))


# | -or   ;    & -and
print(mov_df[(mov_df['director']=='Ridley Scott') | (mov_df['director']=='Christopher Nolan')])
print(mov_df[mov_df['director'].isin(['Christopher Nolan','Ridley Scott'])].head())

# in case  we want movier from 2005 to 2010
print('=================')
print(mov_df[
    ((mov_df['year']>=2005) & (mov_df['year']<=2010)) &
    (mov_df['rating']>8.0) &
    (mov_df['revenue_millions'] < mov_df['revenue_millions'].quantile(0.25))
    ])

# ---- applying custom functions 
def rating_fun(x):
    if x >= 8.0:
        return "good"
    else:
        return "bad"
mov_df["rating_category"] = mov_df["rating"].apply(rating_fun)

# ---- Examples with ploting of data 

mov_df.plot(kind='scatter',x='rating',y='revenue_millions',title='Rating vs Revenue')
plt.grid(True)
plt.show()

#--- histogram
mov_df['revenue_millions'].plot(kind='histogram',title='Revenue (millions)')
plt.show()


# ---- candle like graphs, box 
mov_df['revenue_millions'].plot(kind='box')
plt.show()

