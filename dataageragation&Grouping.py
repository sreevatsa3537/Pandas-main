import pandas as pd
c1=pd.Series([19,20,83,44,35]) # To create a series of numbers
c2=pd.Series(['A','B','A','B','A']) # To create a series of categories
data1=pd.DataFrame({'Name':c2,'Drink':c1}) # To create a dataframe from the two series
grouped=data1.groupby('Name') # To group the dataframe by the 'Name' column
print(grouped.sum()) # To get the sum of the 'Drink' column for each group it will add a dn b and show the sum for each group
pv=data1.pivot_table(values='Drink',index='Name') # To create a pivot table from the dataframe it will give the same result as groupby but in a different format
print(pv) ## we did not guve any aggfunc so it will take the mean by default but we can specify any aggfunc like sum, count, etc
print("---------------------------------------------------------------------------------------")
cross=pd.crosstab(data1['Name'],data1['Drink']) # To create a cross tabulation from the dataframe it will show the count of each combination of 'Name' and 'Drink'
print(cross) ## it will show the count of each combination of 'Name' and 'Drink' in the dataframe it will show how many times A and 19, A and 20, A and 83, A and 44, A and 35, B and 19, B and 20, B and 83, B and 44, B and 35 are present in the dataframe
# bool 1meaning true and 0 meaning false so it will show the count of each combination of 'Name' and 'Drink' in the dataframe it will show how many times A and 19, A and 20, A and 83, A and 44, A and 35, B and 19, B and 20, B and 83, B and 44, B and 35 are present in the dataframe
## concatination and merging
b=pd.Series(['A','B','A','C','B','C','A']) # To create another series of categories
data2=pd.DataFrame({'Name':b,'Age':[25,30,35,40,45,50,55]}) # To create another dataframe from the series       
con=pd.concat([data1,data2])
print(con) # To concatenate the two dataframes it will combine the two dataframes vertically by default
pd.merge(data1,data2,on='Name') # To merge the two dataframes on the 'Name' column it will combine the two dataframes based on the common values in the 'Name' column it will show only the rows where the 'Name' column has common values in both dataframes
data1.join(data2.set_index9('Name'),on='Name') # To join the two dataframes on the 'Name' column it will combine the two dataframes based on the common values in the 'Name' column it will show all the rows from the left dataframe and the matching rows from the right dataframe it will show NaN for the non-matching rows in the right dataframe  
# Diff bw merge and join is merge applys inner join by default and join applies left join by default but we can specify the type of join we want to apply in both merge and join functions