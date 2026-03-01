import numpy as np
import pandas as pd
a=pd.DataFrame({
    'Name':['Alice','Bob','Charlie','David','Eva','Frank','Grace','Hannah','Ian','Jack'],
    'gender':['F','M','M','M','F','M','F','F','M','M'],
    'Age':[25,30,35,40,45,50,55,60,65,70],
    'salary':['15k','6k','71k','38k','69k','170k','191k','12k','139k','24k']
})
a.to_csv('data.csv',index=False) # To save the dataframe to a csv file index=false means we don't want to save the index of dataframe to csv file
data=pd.read_csv('data.csv') # To read the csv file and create a dataframe from it
print(data)
## some other ways to create create a dataframe
dict={
    'x':[1,2,3,4,5],
    'y':np.array([10,20,30,40,50]),
    'z':50 # 50 will be repeated for all rows in column z
}
df=pd.DataFrame(dict) # To create a dataframe from a dictionary
print(df)
narr=np.array([[1,2,3],[4,5,6],[7,8,9]]) # To create a dataframe from a numpy array
df2=pd.DataFrame(narr,columns=['Numpy','Numpy','Numpy']) # To create a dataframe from a numpy array and assign column names to it
print(df2)
## data cleaning and preprocessing
# Handeling missing values
missing=pd.Series([1,2,None,4,5]) # To create a series with some missing values
missing.dropna() # To drop the missing values from the series
missing.fillna(0) # To fill the missing values with 0
missing.fillna(missing.mean()) # To fill the missing values with the mean of the series
# REmoving duplicates
dup1=pd.Series([1,2,3,4,5,1,2,3]) # To create a series with some duplicate values
dup2=pd.Series([1,20,3,40,5,1,20,3]) # To create another series with some duplicate values
duplicate=pd.DataFrame({'C1':dup1,'C2':dup2}) # To create a dataframe from the two series
print(duplicate.drop_duplicates()) # To drop the duplicate rows from the dataframe only 1 1,1 and 3,3 will be kept
data.replace('k','M',regex=True,inplace=True) # To replace 'k' with 'M' in the salary column of the dataframe
# regex= trues is imp cause there is no k seperately it is stuck with the number so we need to use regex to replace it
print(data)
# us .astype to convert the type from int to float or string to int etc

########## STring Operations
str1=pd.Series(['Hello World','Python is great','Data Science is fun']) # To create a series of strings
print(str1.str.upper()) # To convert the strings to uppercase