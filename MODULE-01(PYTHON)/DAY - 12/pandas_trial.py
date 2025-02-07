import pandas as pd
data={
    'Name':['Alice', 'Bob', 'Charlie', 'David'],
    'Age':[25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df=pd.DataFrame(data)
# print(df)      #prints the 
# display.df()  #Gives warning and does not execute
# df=pd.read_csv('DAY - 12/industry.csv')
# print(df)
df=pd.read_csv('DAY - 12/Book1.csv')
# df7=df[df['Age']>20]
# print(df7)

#Grouping Data step-9
df9=df.groupby('Name').count()
print(df9)