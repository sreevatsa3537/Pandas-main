import pandas as pd
a=pd.DataFrame({
    'Name':['Alice','Bob','Charlie','David','Eva'],
    'Lemonades sold':[5,3,8,6,2],
    'price per coustmer':[150,90,240,180,30]
})
print(a)
#### OR USING SERIES ####
c1=pd.Series(['Alice','Bob','Charlie','David','Eva'])
c2=pd.Series([5,3,8,6,2])
c3=pd.Series([150,90,240,180,30])
output=pd.DataFrame({
    'Column1':c1,
    'COlumn2':c2,
    'Column3':c3
})
print(output)
print(a.shape) # to know the shape of dataframe
print("---------------------------------------------------------------------------------------------------------------")
### ACCESSING DATA FROM DATAFRAME ###
## There are two types of indexing: 1. loc 2. iloc
print(a.loc[1,'Lemonades sold']) # access data using loc (label based indexing) we use colunm name here like name if we had changed
# the index to something else and columns name is also seperate so we use them 
print(a.iloc[0,0]) # access data using iloc (integer based indexing) likefor second colunm instead of using Lemonades sold we use [0,1]
print(a.info()) # to get the information about dataframe like number of non null values and datatype of each column
print(a.describe()) # to get the statistical summary of numerical columns in dataframe like count, mean, std, min, max etc.
# Filtering data in dataframe
filtered_data=a[a['Lemonades sold']>4]
print(filtered_data) # to filter the data based on condition like here we are filtering the data where lemonades sold is greater than 4
a['Tips']=a['price per coustmer']*0.1 # To add a new columnto the dataframe
print(a)
# *********************************************************************************
# TO delete we have 2 methods 1. drop() 2. del keyword
# a=a.drop(columns=['Tips'])
# del a['Tips']
# *********************************************************************************
a.loc[a['Lemonades sold'] == 2,'Lemonades sold'] = 7 # To update the value in dataframe where lemonades sold is 2 we are changing it to 7
# Now pandas knows:rows → where Lemonades sold == 2 column → Lemonades sold value → 7
print(a)
a.rename(columns={'price per coustmer':'Total bill'}, inplace=True) # To rename the column name in dataframe inplace=true means we want 
# to change the original dataframe if we set it to false then it will return a new dataframe with the changed column name
# but original dataframe will remain same
a['Total bill']=a['Total bill'].replace(30,210) # To replace the value in dataframe where total bill is 30 we are changing it to 210
a['Tips']=a['Tips'].replace(3,21) # To replace the value in dataframe where tips is 3 we are changing it to 21
print(a)
## WE want to set an column as index of dataframe we can use set_index() method
a.set_index('Name',inplace=True) # To set the column name as index of dataframe inplace=true means we want to change the original dataframe
print(a)
print(a.loc['David','Total bill']) # To access the data using loc after setting the index we can use the index name to access the data
print(a.iloc[2,1]) # To access the data using iloc after setting the
## we can also set multiple columns as index of dataframe by passing a list of column names to set_index() method
multi_index=pd.DataFrame({
    'park':['Yellowstone','Yosemite','Grand Canyon','Zion','Rocky Mountain'],
    'state':['Wyoming','California','Arizona','Utah','Colorado'],
    'visitors':[4000000,5000000,6000000,3000000,2000000]
}).set_index(['park','state']) # To set multiple columns as index of dataframe
print(multi_index)
print(multi_index.loc[('Yellowstone','Wyoming')]) # To access the data using loc after setting multiple
# columns as index we can use the index names to access the data