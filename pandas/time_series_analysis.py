import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# till now
# Timestamp
print(pd.Timestamp('6th jan 2023 8:10'))
# DatetimeIndex -> df and series index
print(pd.DatetimeIndex([pd.Timestamp('6th jan 2023 8:10'),pd.Timestamp('7th jan 2023 8:10'),pd.Timestamp('8th jan 2023 8:10')]))
# date_range()
print(pd.date_range(start='2023-1-6',end='2023-1-31',freq='D'))
# to_datetime()
s = pd.Series(['2023/1/6','2023/1/7','2023/1/7'])
print(pd.to_datetime(s))
print(pd.to_datetime(s).dt.day_name())

# Timedelta Object
# Represents a duration, the difference between two dates or times.

# create using Timestamp objects
t1 = pd.Timestamp('6th Jan 2023 8:20:14')
t2 = pd.Timestamp('26th Jan 2023 10:00:00')

print(t2 - t1)

# standalone creation
print(pd.Timedelta(days=2,hours=10,minutes=35))

# Arithmetic
print(pd.Timestamp('6th jan 2023') + pd.Timedelta(days=2,hours=10,minutes=35))

print(pd.date_range(start='2023-1-6',end='2023-1-31',freq='D') - pd.Timedelta(days=2,hours=10,minutes=35))

# real life example
df = pd.read_csv(r'pandas\deliveries.csv')
print(df.head())

df['order_date'] = pd.to_datetime(df['order_date'])
df['delivery_date'] = pd.to_datetime(df['delivery_date'])

df['delivery_time_period'] = df['delivery_date'] - df['order_date']
print(df['delivery_time_period'])
print(df['delivery_time_period'].mean())

# Time series
# A time series is a data set that tracks a sample over time. In particular, a time series allows one to see what factors influence certain variables from period to period. Time series analysis can be useful to see how a given asset, security, or economic variable changes over time.

# Examples

# Financial Data (Company stocks)
# Natural Data (Rainfall measurement)
# Event Data (Covid)
# Medical Data (Heart rate monitoring)
# Types of Operations done on Time Series

# Time Series Analysis
# Time Series Forecasting

google = pd.read_csv(r'pandas\google.csv')
print(google.head())
print(google.tail())

google.info()

google['Date'] = pd.to_datetime(google['Date'])
print(google['Date'])

google.info()

google.set_index('Date',inplace=True)
print(google.head())

# fetch a specific date
print(google.loc['2021-12-30'])

# partial indexing -> select a particular year/month
print(google.loc['2018-12'])
print(google.loc['2018'])

google['month_name'] = google.index.month_name()
google['weekday_name'] = google.index.day_name()
google['quarter'] = google.index.quarter

print(google.head())

# slicing
print(google.loc['2018-12-15':'2019-1-1':2])

# challenge -> fetch info for a particular date every year -> limitation of timedelta

print(google[google.index.isin(pd.date_range(start='2005-1-6',end='2022-1-6',freq=pd.DateOffset(years=1)))])

# viz a single col
google['Close'].plot()
plt.show()

# 2
google.loc['2021-12']['Close'].plot()
plt.show()

# 3
google.groupby('month_name')['Close'].mean().plot(kind='bar')
plt.show()

# quaterly trend
google.groupby('quarter')['Close'].mean().plot(kind='bar')
plt.show()

# frequency
print(google.index)

# asfreq
print(google.asfreq('6H',method='bfill'))

# Resampling
# Resampling involves changing the frequency of your time series observations.

# Two types of resampling are:

# Upsampling: Where you increase the frequency of the samples, such as from minutes to seconds.
# Downsampling: Where you decrease the frequency of the samples, such as from days to months.

# Upsampling
google['Close'].resample('12H').interpolate(method='spline',order=2).plot()
plt.show()

# Rolling Window(Smoothing)
# Time series data in original format can be quite volatile, especially on smaller aggregation levels. The concept of rolling, or moving averages is a useful technique for smoothing time series data.
# Rolling window
# yt['Subscribers'].rolling(30).mean().plot(title='rolling')
# yt['Subscribers'].ewm(30).mean().plot(title='ewm')

# Shifting
# The shift() function is Pandas is used to, well, shift the entire series up or down by the desired number of periods.
# yt['Subscribers'].shift(-1)

# shift example
df = pd.read_csv(r'pandas\login.csv',header=None)
df = df[[1,2]]
print(df.head())
df.rename(columns={1:'user_id',2:'login_time'},inplace=True)
print(df.head())

user_df = df[df['user_id'] == 458]
print(user_df.head())

user_df['login_time'] = pd.to_datetime(user_df['login_time'])
user_df.info()

user_df['shifted'] = user_df['login_time'].shift(1)
print((user_df['login_time'] - user_df['shifted']).mean())