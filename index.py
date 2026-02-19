import pandas as pd
a=pd.Series([199,22,35,4,15,16])
print(a[2:])
print(a.head(3)) # used to see first 5 elements sample of data if we dont pass any value it will consider 5 as default
print(a.tail(3)) # used to see last 5 elements sample of data if we dont pass any value it will consider 5 as default
print(a.sort_values()) # sort the values in ascending order
print(a.count()) # count the number of non null values
print(a.isnull()) # check for null values
print(a*4) # multiply each value by 4
b=pd.Series([100,2,320,41,15,None])
print(b.isnull())
print(b.fillna(0)) # fill null values with 0
indx=pd.Series([1,2,3,4,5,667],index=list('abcdef'))
print(indx)