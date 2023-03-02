# What is Pandas
# Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.

# Pandas Series
# A Pandas Series is like a column in a table. It is a 1-D array holding data of any type.

# Importing Pandas
import numpy as np
import pandas as pd

# Series from lists
# string
country = ['india','pakistan','nepal','usa']

print(pd.Series(country))

# integers
runs = [13,24,56,78,100]

runs_ser = pd.Series(runs)
print(runs_ser)

# custom index
marks = [67,57,89,100]
subjects = ['maths','english','science','hindi']

print(pd.Series(marks,index=subjects))

# setting a name
marks = pd.Series(marks,index=subjects,name='Rajnish ke marks')
print(marks)

# Series from dict
marks = {
    'maths':67,
    'english':57,
    'science':89,
    'hindi':100
}

marks_series = pd.Series(marks,name='Rajnish ke marks')
print(marks_series)

# Series Attributes

# size
print(marks_series.size)

# dtype
print(marks_series.dtype)

# name
print(marks_series.name)

# is_unique
print(marks_series.is_unique)

print(pd.Series([1,1,2,3,4,5]).is_unique)

# index
print(marks_series.index)

print(runs_ser.index)

# values
print(marks_series.values)

# Series using read_csv

# with one col
subs = pd.read_csv(r'C:/Users/rajni/OneDrive/Documents/PycharmProjects/RajnishProject/.idea/pandas/datasets-session-16/subs.csv',squeeze=True)
print(subs)

# with 2 cols
vk = pd.read_csv(r'C:/Users/rajni/OneDrive/Documents/PycharmProjects/RajnishProject/.idea/pandas/datasets-session-16/kohli_ipl.csv',index_col='match_no',squeeze=True)
print(vk)

movies = pd.read_csv(r'C:/Users/rajni/OneDrive/Documents/PycharmProjects/RajnishProject/.idea/pandas/datasets-session-16/bollywood.csv',index_col='movie',squeeze=True)
print(movies)

# Series methods

# head ---> return the first five digit
print(subs.head())

print(vk.head(3))
# tail ---> return the last five digit
print(movies.tail())

print(vk.tail(10))

# sample ---> return random anyone
print(movies.sample(5))

# value_counts -> movies --> return about frequency
print(movies.value_counts())

# sort_values -> values are sorted by the values
# inplace  --> change in original path
print(vk.sort_values())   #--> in ascending order

print(vk.sort_values(ascending=False)) #---> in desending number

print(vk.sort_values(ascending=False).head(1).values[0])

# print(vk.sort_values(inplace = True))

# sort_index -> values are sorted by the index

# movies.sort_index(ascending=False,inplace=True)
# print(movies)

print(movies.sort_index(ascending=False))

# Series Maths Methods
# count ---> without nan value
print(vk.count())

# sum -> product
print(subs.sum())
print(subs.product())

# mean -> median -> mode -> std -> var
print(subs.mean())
print(vk.median())
print(movies.mode())
print(subs.std())
print(vk.var())

# min/max
print(subs.max())
print(subs.min())

# describe
print(subs.describe())

# Series Indexing

# integer indexing
x = pd.Series([12,13,14,35,46,57,58,79,9])
print(x[0])
print(movies[2])

# negative indexing
# print(x[-1])   ---> negative indexing is not work on integer index
print(movies[-2])
# print(vk[-1])
print(marks_series[-1])

# slicing
print(vk[5:16])

# negative slicing  ---> negative slicing is work on every datatype
print(vk[-5:])
print(movies[::2])

# fancy indexing
print(vk[[1,3,4,5]])

# indexing with labels -> fancy indexing
print(movies['2 States (2014 film)'])

# Editing Series

# using indexing
marks_series[1] = 100
print(marks_series)

# what if an index does not exist
marks_series['evs'] = 100
print(marks_series)

# slicing
runs_ser[2:4] = [100,100]
print(runs_ser)

# fancy indexing
runs_ser[[0,3,4]] = [0,0,0]
print(runs_ser)

# using index label
movies['2 States (2014 film)'] = 'Alia Bhatt'
print(movies)

# Series with Python Functionalities

# len/type/dir/sorted/max/min
print(len(subs))
print(type(subs))
print(dir(subs))
print(sorted(subs))
print(min(subs))
print(max(subs))

# type conversion
print(list(marks_series))

print(dict(marks_series))

# membership operator

print('2 States (2014 film)' in movies)

print('alia Bhatt' in movies.values)

# looping
for i in movies.index:
  print(i)

# Arithmetic Operators(Broadcasting)
print(100 + marks_series)

# Relational Operators
print(vk >= 50)

# Boolean Indexing on Series

# Find no of 50's and 100's scored by kohli
print(vk[vk >= 50].size)

# find number of ducks
print(vk[vk == 0].size)

# Count number of day when I had more than 200 subs a day
print(subs[subs > 200].size)

# find actors who have done more than 20 movies
num_movies = movies.value_counts()
print(num_movies[num_movies > 20])

# Plotting Graphs on Series
import matplotlib.pyplot as plt
# 1
subs.plot()
plt.show()
# 2
movies.value_counts().head(20).plot(kind='pie')
plt.show()

# Some Important Series Methods
print(subs)
# astype
import sys
print(sys.getsizeof(vk))
print(sys.getsizeof(vk.astype('int16')))

# between
bet = vk.between(51,99)
print(vk[bet].size)

#clip
print(subs.clip(100,200))

# drop_duplicates
temp = pd.Series([1,1,2,2,3,3,4,4])
print(temp)

print(temp.drop_duplicates())
print(temp.drop_duplicates(keep='last'))

# duplicated
print(temp.duplicated().sum())
print(vk.duplicated().sum())
print(movies.drop_duplicates())

# size and count 
temp = pd.Series([1,2,3,np.nan,5,6,np.nan,8,np.nan,10])
print(temp)

print(temp.size)
print(temp.count())

# isnull
print(temp.isnull().sum())

# dropna
print(temp.dropna())

# fillna
print(temp.fillna(0))

# isin
print(vk[(vk == 49) | (vk == 99)])

print(vk[vk.isin([49,99])])

# apply
print(movies)

print(movies.apply(lambda x:x.split()[0].upper()))

print(subs.apply(lambda x:'good day' if x > subs.mean() else 'bad day'))

# copy
print(vk)
new = vk.head()
print(new)

new[1] = 1
print(vk)
#
new = vk.head().copy()
new[1] = 100
print(new)
print(vk)