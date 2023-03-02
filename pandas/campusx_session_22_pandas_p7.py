# pandas string 
import numpy as np 
import pandas as pd 

# What are vectorized operations
a = np.array([1,2,3,4])
print(a * 4)

# problem in vectorized opertions in vanilla python
'''s = ['cat','mat',None,'rat']

print([i.startswith('c') for i in s])'''

# How pandas solves this issue?

s = pd.Series(['cat','mat',None,'rat'])
# string accessor
print(s.str.startswith('c'))
# fast and optimized

df = pd.read_csv(r'pandas\titanic.csv')
print(df.head())

# Common Functions
# lower/upper/capitalize/title
print(df['Name'].str.upper())

print(df['Name'].str.capitalize())

print(df['Name'].str.title())
# len
print(df['Name'].str.len())

print(df['Name'][df['Name'].str.len() == 82].values[0])

# strip
print("                   rajnish                             ".strip())

print(df['Name'].str.strip())

# split -> get
df['lastname'] = df['Name'].str.split(',').str.get(0)
print(df.head())
#
df[['title','firstname']] = df['Name'].str.split(',').str.get(1).str.strip().str.split(' ', n=1, expand=True)
print(df.head())
#
print(df['title'].value_counts())

# replace
df['title'] = df['title'].str.replace('Ms.','Miss.')
df['title'] = df['title'].str.replace('Mlle.','Miss.')

print(df['title'].value_counts())

# filtering
# startswith/endswith
print(df[df['firstname'].str.startswith('R')])
print(df[df['firstname'].str.endswith('A')])
# isdigit/isalpha...
print(df[df['firstname'].str.isdigit()])

# applying regex
# contains
# search john -> both case
print(df[df['firstname'].str.contains('john',case=False)])
# find lastnames with start and end char vowel
print(df[df['lastname'].str.contains('^[^aeiouAEIOU].+[^aeiouAEIOU]$')])

# slicing
print(df['Name'].str[::-1])

################### Date and Time in Pandas ########################

import numpy as np
import pandas as pd

# Timestamp Object
# Time stamps reference particular moments in time (e.g., Oct 24th, 2022 at 7:00pm)

# Creating Timestamp objects

# creating a timestamp
print(pd.Timestamp('2023/1/5'))
print(type(pd.Timestamp('2023/1/5')))

# variations
print(pd.Timestamp('2023-1-5'))
print(pd.Timestamp('2023, 1, 5'))

# only year
print(pd.Timestamp('2023'))

# using text
print(pd.Timestamp('5th January 2023'))

# providing time also
# AM and PM
print(pd.Timestamp('5th January 2023 9:21AM'))
# pd.Timestamp('2023/1/5/9/21')

# using datetime.datetime object
import datetime as dt

x = pd.Timestamp(dt.datetime(2023,1,5,9,21,56))
print(x)

# fetching attributes
print(x.year)
print(x.month)
print(x.day)
print(x.hour)
print(x.minute)
print(x.second)

# why separate objects to handle data and time when python already has datetime functionality?
# syntax wise datetime is very convenient
# But the performance takes a hit while working with huge data. List vs Numpy Array
# The weaknesses of Python's datetime format inspired the NumPy team to add a set of native time series data type to NumPy.
# The datetime64 dtype encodes dates as 64-bit integers, and thus allows arrays of dates to be represented very compactly.

import numpy as np
date = np.array('2015-07-04',dtype=np.datetime64)
print(date)
print(type(date))

print(date + np.arange(12))
# Because of the uniform type in NumPy datetime64 arrays, this type of operation can be accomplished much more quickly than if we were working directly with Python's datetime objects, especially as arrays get large

# Pandas Timestamp object combines the ease-of-use of python datetime with the efficient storage and vectorized interface of numpy.datetime64

# From a group of these Timestamp objects, Pandas can construct a DatetimeIndex that can be used to index data in a Series or DataFrame

# DatetimeIndex Object
# A collection of pandas timestamp

# from strings
print(pd.DatetimeIndex(['2023/1/1','2022/1/1','2021/1/1']))
print(type(pd.DatetimeIndex(['2023/1/1','2022/1/1','2021/1/1'])))

# using python datetime object
print(pd.DatetimeIndex([dt.datetime(2023,1,1),dt.datetime(2022,1,1),dt.datetime(2021,1,1)]))

# using pd.timestamps
dt_index = pd.DatetimeIndex([pd.Timestamp(2023,1,1),pd.Timestamp(2022,1,1),pd.Timestamp(2021,1,1)])
print(dt_index)

# using datatimeindex as series index

print(pd.Series([1,2,3],index=dt_index))

# date_range function

# generate daily dates in a given range
print(pd.date_range(start='2023/1/5',end='2023/2/28',freq='D'))

# alternate days in a given range
print(pd.date_range(start='2023/1/5',end='2023/2/28',freq='2D'))

# B -> business days
print(pd.date_range(start='2023/1/5',end='2023/2/28',freq='B'))

# W -> one week per day
print(pd.date_range(start='2023/1/5',end='2023/2/28',freq='W-THU'))

# H -> Hourly data(factor)
print(pd.date_range(start='2023/1/5',end='2023/2/28',freq='6H'))

# M -> Month end
print(pd.date_range(start='2023/1/5',end='2023/2/28',freq='M'))

# MS -> Month start
print(pd.date_range(start='2023/1/5',end='2023/2/28',freq='MS'))

# A -> Year end
print(pd.date_range(start='2023/1/5',end='2030/2/28',freq='A'))

# using periods(number of results)
print(pd.date_range(start='2023/1/5',periods=25,freq='M'))

# to_datetime function
# converts an existing objects to pandas timestamp/datetimeindex object

# simple series example

s = pd.Series(['2023/1/1','2022/1/1','2021/1/1'])
print(pd.to_datetime(s).dt.day_name())

# with errors
s = pd.Series(['2023/1/1','2022/1/1','2021/130/1'])
print(pd.to_datetime(s,errors='coerce').dt.month_name())

# work on csv data 
df = pd.read_csv(r'pandas\expense_data.csv')
print(df)

df['Date'] = pd.to_datetime(df['Date'])
print(df.head())

print(df.info())

# dt accessor --> Accessor object for datetimelike properties of the Series values.

print(df['Date'].dt.is_quarter_start)

# plot graph
import matplotlib.pyplot as plt
plt.plot(df['Date'],df['INR'])
plt.show()

# day name wise bar chart

df['day_name'] = df['Date'].dt.day_name()
print(df.head())
df.groupby('day_name')['INR'].mean().plot(kind='bar')
plt.show()
# month wise bar chart

df['month_name'] = df['Date'].dt.month_name()
print(df.head())
df.groupby('month_name')['INR'].mean().plot(kind='bar')
plt.show()
##################
print(df[df['Date'].dt.is_month_end])