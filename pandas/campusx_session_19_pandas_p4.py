# groupby in pandas 
import pandas as pd
import numpy as np

movies = pd.read_csv(r'C:\Users\rajni\OneDrive\Documents\PycharmProjects\RajnishProject\.idea\pandas\imdb-top-1000.csv')
print(movies.head())

genres = movies.groupby('Genre')
print(genres)

# Applying builtin aggregation fuctions on groupby objects
print(genres.std())

# find the top 3 genres by total earning
'''print(movies.groupby('Genre').sum()['Gross'].sort_values(ascending=False).head(3))

print(movies.groupby('Genre')['Gross'].sum().sort_values(ascending=False).head(3))'''

# find the genre with highest avg IMDB rating
print(movies.groupby('Genre')['IMDB_Rating'].mean().sort_values(ascending=False).head(1))

# find director with most popularity
print(movies.groupby('Director')['No_of_Votes'].sum().sort_values(ascending=False).head(1))

# find the highest rated movie of each genre
print(genres['IMDB_Rating'].max())

# find number of movies done by each actor
# movies['Star1'].value_counts()

print(movies.groupby('Star1')['Series_Title'].count().sort_values(ascending=False))

# GroupBy Attributes and Methods

# find total number of groups -> len
print(len(movies.groupby('Genre')))
print(movies['Genre'].nunique())

# find items in each group -> size
print(movies.groupby('Genre').size())

# first()/last() -> nth item
genres = movies.groupby('Genre')
print(genres.first())
print(genres.last())
print(genres.nth(6))

# get_group -> vs filtering
print(movies['Genre'].value_counts())

print(genres.get_group('Fantasy'))
# print(movies[movies['Genre'] == 'Fantasy'])

# groups
print(genres.groups)

# describe
print(genres.describe())

# sample
print(genres.sample(2,replace=True))

# nunique
print(genres.nunique())

# agg method
# passing dict
print(genres.agg(
    {
        'Runtime':'mean',
        'IMDB_Rating':'mean',
        'No_of_Votes':'sum',
        'Gross':'sum',
        'Metascore':'min'
    }
))

# passing list
print(genres.agg(['min','max','mean','sum']))

# Adding both the syntax
print(genres.agg(
    {
        'Runtime':['min','mean'],
        'IMDB_Rating':'mean',
        'No_of_Votes':['sum','max'],
        'Gross':'sum',
        'Metascore':'min'
    }
))

# looping on groups
df = pd.DataFrame(columns=movies.columns)
for group,data in genres:
  df = df.append(data[data['IMDB_Rating'] == data['IMDB_Rating'].max()])

print(df)

# split (apply) combine
# apply -> builtin function

print(genres.apply(min))

# find number of movies starting with A for each group

def foo(group):
  return group['Series_Title'].str.startswith('A').sum()

print(genres.apply(foo))

# find ranking of each movie in the group according to IMDB score

def rank_movie(group):
  group['genre_rank'] = group['IMDB_Rating'].rank(ascending=False)
  return group

print(genres.apply(rank_movie))

# find normalized IMDB rating group wise

def normal(group):
  group['norm_rating'] = (group['IMDB_Rating'] - group['IMDB_Rating'].min())/(group['IMDB_Rating'].max() - group['IMDB_Rating'].min())
  return group

print(genres.apply(normal))

# groupby on multiple cols
duo = movies.groupby(['Director','Star1'])
print(duo)

# size
print(duo.size())

# get_group
print(duo.get_group(('Aamir Khan','Amole Gupte')))

# find the most earning actor->director combo
print(duo['Gross'].sum().sort_values(ascending=False).head(1))

# find the best(in-terms of metascore(avg)) actor->genre combo
print(movies.groupby(['Star1','Genre'])['Metascore'].mean().reset_index().sort_values('Metascore',ascending=False).head(1))

# agg on multiple groupby
print(duo.agg(['min','max','mean']))

# Exercise 
ipl = pd.read_csv(r'C:\Users\rajni\OneDrive\Documents\PycharmProjects\RajnishProject\.idea\pandas\deliveries.csv')
print(ipl.head())

print(ipl.shape)

# find the top 10 batsman in terms of runs
print(ipl.groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False).head(10))

# find the batsman with max no of sixes
six = ipl[ipl['batsman_runs'] == 6]

print(six.groupby('batsman')['batsman'].count().sort_values(ascending=False).head(1).index[0])

# find batsman with most number of 4's and 6's in last 5 overs
temp_df = ipl[ipl['over'] > 15]
temp_df = temp_df[(temp_df['batsman_runs'] == 4) | (temp_df['batsman_runs'] == 6)]
print(temp_df.groupby('batsman')['batsman'].count().sort_values(ascending=False).head(1).index[0])

# find V Kohli's record against all teams
temp_df = ipl[ipl['batsman'] == 'V Kohli']

print(temp_df.groupby('bowling_team')['batsman_runs'].sum().reset_index())

# Create a function that can return the highest score of any batsman

def highest(batsman):
  temp_df = ipl[ipl['batsman'] == batsman]
  return temp_df.groupby('match_id')['batsman_runs'].sum().sort_values(ascending=False).head(1).values[0]

print(highest('V Kohli'))
print(highest('DA Warner'))