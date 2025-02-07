import pandas as pd

data = {
    'Region': ['North', 'North', 'South', 'South', 'East', 'East'],
    'State': ['Delhi', 'Punjab', 'Tamil Nadu', 'Karnataka', 'TG', 'Odisha'],
    'Year': [2021, 2022, 2021, 2022, 2021, 2022],
    'Sales': [750000, 820000, 690000, 720000, 670000, 710000],
    'Profit': [95000, 102000, 85000, 91000, 77000, 88000]
}
df=pd.DataFrame(data)
# df.set_index(['Region', 'State', 'Year'], inplace=True)
# print(df)

#selecting specific data from a multi-indexed DataFrame
# print(df.loc[('South','Tamilnadu',2021), 'Sales'])
# print(df1)

#Merging and joining
df_sales=pd.DataFrame({'State':['Delhi', 'Tamil Nadu', 'West Bengal'],
'Sales':[1570000, 1410000, 1380000]})
df_profit=pd.DataFrame({'State': ['Delhi', 'Tamil Nadu', 'West Bengal'],
'Profit':[185000, 165000, 155000]})
df_merged=pd.merge(df_sales, df_profit, on='State', how='inner')
print(df_merged)

# import pandas as pd
# data=[]
# m=int(input("enter the number of records: "))
# for i in range(n):
#     name=input("Ejter name: ")
#     age=input("Enter Age: ")
#     data.append({"Name": name, "Age":age},"Inder":i+1)

# df=pd.DataFrame(data).set_index("Index")
# df_sorted=df.sort_values()