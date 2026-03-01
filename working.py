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
df2=pd.DataFrame(narr,columns=['NA','NB','NC']) # To create a dataframe from a numpy array and assign column names to it
print(df2)
