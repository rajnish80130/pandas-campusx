import numpy as np
import pandas as pd

# Series is 1D and DataFrames are 2D objects
# But why?
# And what exactly is index?

# can we have multiple index? Let's try
index_val = [('cse',2019),('cse',2020),('cse',2021),('cse',2022),('ece',2019),('ece',2020),('ece',2021),('ece',2022)]
a = pd.Series([1,2,3,4,5,6,7,8],index=index_val)
print(a)
print(a['cse',2022])

# The problem?
# print(a['cse'])

# The solution -> multiindex series(also known as Hierarchical Indexing)
# multiple index levels within a single index

# how to create multiindex object
# 1. pd.MultiIndex.from_tuples()
index_val = [('cse',2019),('cse',2020),('cse',2021),('cse',2022),('ece',2019),('ece',2020),('ece',2021),('ece',2022)]
multiindex = pd.MultiIndex.from_tuples(index_val)
print(multiindex)

# level inside multiindex object
print(multiindex.levels[0])   #level find the column through index

# 2. pd.MultiIndex.from_product()
print(pd.MultiIndex.from_product([['cse','ece'],[2019,2020,2021,2022]]))

# creating a series with multiindex object
s = pd.Series([1,2,3,4,5,6,7,8],index=multiindex)
print(s)

# how to fetch items from such a series
print(s['cse'])

# unstack --->row ko column banana
temp = s.unstack()
print(temp)

# stack  ---> column ko row banana
print(temp.stack())

# multiindex dataframe

branch_df1 = pd.DataFrame(
    [
        [1,2],
        [3,4],
        [5,6],
        [7,8],
        [9,10],
        [11,12],
        [13,14],
        [15,16],
    ],
    index = multiindex,
    columns = ['avg_package','students']
)

print(branch_df1)
print(branch_df1['students'])
print(branch_df1.loc['cse'])
print(branch_df1.loc['cse',2019])

# multiindex df from columns perspective
branch_df2 = pd.DataFrame(
    [
        [1,2,0,0],
        [3,4,0,0],
        [5,6,0,0],
        [7,8,0,0],
    ],
    index = [2019,2020,2021,2022],
    columns = pd.MultiIndex.from_product([['delhi','mumbai'],['avg_package','students']])
)

print(branch_df2)

print(branch_df2.iloc[0])
print(branch_df2.loc[2019])
print(branch_df2.loc[:,('delhi','students')])

# Multiindex df in terms of both cols and index

branch_df3 = pd.DataFrame(
    [
        [1,2,0,0],
        [3,4,0,0],
        [5,6,0,0],
        [7,8,0,0],
        [9,10,0,0],
        [11,12,0,0],
        [13,14,0,0],
        [15,16,0,0],
    ],
    index = multiindex,
    columns = pd.MultiIndex.from_product([['delhi','mumbai'],['avg_package','students']])
)

print(branch_df3)

# Stacking and Unstacking

# unstack ---> column ko row me change krna
print(branch_df3)
print(branch_df3.unstack().unstack())

# stack ---> row ko column me change krna
print(branch_df3)
print(branch_df3.stack().stack())

# Working with multiindex dataframes

# head and tail
print(branch_df3.head())
# shape
print(branch_df3.shape)
# info
branch_df3.info()
# duplicated -> isnull
print(branch_df3.duplicated())
print(branch_df3.isnull())

# Extracting rows single
print(branch_df3.loc[('cse',2022)])

# multiple
print(branch_df3.loc[('cse',2019):('ece',2020):2])

# using iloc
print(branch_df3.iloc[0:5:2])

# Extracting cols
print(branch_df3['delhi']['students'])

print(branch_df3.iloc[:,1:3])

# Extracting both
print(branch_df3.iloc[[0,4],[1,2]])

# sort index
# both -> descending -> diff order
# based on one level
print(branch_df3.sort_index(ascending=False))
print(branch_df3.sort_index(ascending=[False,True]))
print(branch_df3.sort_index(level=0,ascending=[False]))  #--> sort the index 0

# multiindex dataframe(col) -> transpose
print(branch_df3.transpose())

# swaplevel
print(branch_df3.swaplevel(axis=0))
print(branch_df3.swaplevel(axis=1))

# Long Vs Wide Data
# Wide format is where we have a single row for every data point with multiple columns to hold the values of various attributes.

# Long format is where, for each data point we have as many rows as the number of attributes and each row contains the value of a particular attribute for a given data point.

# melt -> simple example branch
# wide to long
print(pd.DataFrame({'cse':[120]}))
print(pd.DataFrame({'cse':[120]}).melt())

# melt -> branch with year
print(pd.DataFrame({'cse':[120],'ece':[100],'mech':[50]}))

print(pd.DataFrame({'cse':[120],'ece':[100],'mech':[50]}).melt(var_name='branch',value_name='num_students'))

# melt on long data
print(pd.DataFrame(
    {
        'branch':['cse','ece','mech'],
        '2020':[100,150,60],
        '2021':[120,130,80],
        '2022':[150,140,70]
    }
))
# convert to long 
print(pd.DataFrame(
    {
        'branch':['cse','ece','mech'],
        '2020':[100,150,60],
        '2021':[120,130,80],
        '2022':[150,140,70]
    }
).melt(id_vars=['branch'],var_name='year',value_name='students'))

# melt -> real world example
death = pd.read_csv(r'pandas\time_series_covid19_deaths_global.csv')
confirm = pd.read_csv(r'pandas\time_series_covid19_deaths_global.csv')

print(death.head())
print(confirm.head())

death = death.melt(id_vars=['Province/State','Country/Region','Lat','Long'],var_name='date',value_name='num_deaths')
confirm = confirm.melt(id_vars=['Province/State','Country/Region','Lat','Long'],var_name='date',value_name='num_cases')

print(death)
print(confirm)

print(confirm.merge(death,on=['Province/State','Country/Region','Lat','Long','date'])[['Country/Region','date','num_cases','num_deaths']])

# pivot table ----> The pivot table takes simple column-wise data as input, and groups the entries into a two-dimensional table that provides a multidimensional summarization of the data.

import numpy as np
import pandas as pd
import seaborn as sns

df = sns.load_dataset('tips')
print(df.head())

#through groupby
print(df.groupby('sex')[['total_bill']].mean())

print(df.groupby(['sex','smoker'])[['total_bill']].mean().unstack())

# through pivot table
print(df.pivot_table(index='sex',columns='smoker',values='total_bill'))   #here default mean

# aggfunc
print(df.pivot_table(index='sex',columns='smoker',values='total_bill',aggfunc='sum'))

# all cols together
print(df.pivot_table(index='sex',columns='smoker'))

print(df.pivot_table(index='sex',columns='smoker')['size'])

# margins
print(df.pivot_table(index='sex',columns='smoker',values='total_bill',aggfunc='sum',margins=True))

# multidimensional
print(df.pivot_table(index=['sex','smoker'],columns=['day','time'],aggfunc='sum',margins=True))

print(df.pivot_table(index=['sex','smoker'],columns=['day','time'],aggfunc={'size':'mean','tip':'max','total_bill':'sum'},margins=True))

# plotting graphs 
df = pd.read_csv(r'pandas\expense_data.csv')
print(df.head())

print(df['Category'].value_counts())

print(df.info())

# add a new column date 
df['Date'] = pd.to_datetime(df['Date'])
print(df.head())

print(df.info())
# add a new column month
df['month'] = df['Date'].dt.month_name()

print(df.head())

import matplotlib.pyplot as plt
# 1
df.pivot_table(index='month',columns='Category',values='INR',aggfunc='sum',fill_value=0).plot()
plt.show()
# 2
df.pivot_table(index='month',columns='Account',values='INR',aggfunc='sum',fill_value=0).plot()
plt.show()
# 3
df.pivot_table(index='month',columns='Income/Expense',values='INR',aggfunc='sum',fill_value=0).plot()
plt.show()