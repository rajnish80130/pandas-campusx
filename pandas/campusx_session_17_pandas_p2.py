import numpy as np
import pandas as pd

# Creating DataFrame
# using lists
student_data = [
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,50,2]
]

print(pd.DataFrame(student_data,columns=['iq','marks','package']))

# using dicts

student_dict = {
    'name':['nitish','ankit','rupesh','rishabh','amit','ankita'],
    'iq':[100,90,120,80,0,0],
    'marks':[80,70,100,50,0,0],
    'package':[10,7,14,2,0,0]
}

students = pd.DataFrame(student_dict)
students.set_index('name',inplace=True)
print(students)

# using read_csv
movies = pd.read_csv(r'C:\Users\rajni\OneDrive\Documents\PycharmProjects\RajnishProject\.idea\pandas\movies.csv')
print(movies)

ipl = pd.read_csv(r'C:\Users\rajni\OneDrive\Documents\PycharmProjects\RajnishProject\.idea\pandas\ipl-matches.csv')
print(ipl)

# DataFrame Attributes and Methods

# shape
print(movies.shape)
print(ipl.shape)

# dtypes    ---> object means string
print(movies.dtypes)
print(ipl.dtypes)

# index
print(movies.index)
print(ipl.index)

# columns
print(movies.columns)
print(ipl.columns)
print(students.columns)

# values
print(students.values)
print(ipl.values)

# head and tail
print(movies.head(2))
print(ipl.tail(2))

# sample
print(ipl.sample(5))

# info
print(movies.info())
print(ipl.info())

# describe
print(movies.describe())
print(ipl.describe())

# mean/max/min/std
print(movies.mean())
print(movies.max())
print(movies.min())
print(movies.std())

# isnull
print(movies.isnull())
print(movies.isnull().sum())

# duplicated
print(movies.duplicated().sum())
print(students.duplicated().sum())

# rename
print(students)
students.rename(columns={'marks':'percent','package':'lpa'},inplace=True)
print(students)

# Math Methods
# sum -> axis argument
print(students.sum(axis=0))   # 0-->column      1-->row
print(students.mean(axis=1))

print(students.var())
print(students.mean())
print(students.max())
print(students.min())
print(students.std())

# Selecting cols from a DataFrame

# single cols
print(movies['title_x'])
print(ipl['Venue'])

# multiple cols
print(movies[['year_of_release','actors','title_x']])
print(ipl[['Team1','Team2','WinningTeam']])

# Selecting rows from a DataFrame
# iloc - searches using index positions
# loc - searches using index labels

# single row
print(movies.iloc[5])

# multiple row
print(movies.iloc[:6])

# fancy indexing
print(movies.iloc[[0,4,5]])

# loc
print(students)
print(students.loc['nitish'])

print(students.loc['nitish':'rishabh':2])

print(students.loc[['nitish','ankita','rupesh']])

print(students.iloc[[0,3,4]])

# Selecting both rows and cols
print(movies.iloc[0:3,0:3])

print(movies.loc[0:2,'title_x':'poster_path'])

# Filtering a DataFrame
print(ipl.head(2))

# find all the final winners
mask = ipl['MatchNumber'] == 'Final'
new_df = ipl[mask]
print(new_df[['Season','WinningTeam']])

# ipl[ipl['MatchNumber'] == 'Final'][['Season','WinningTeam']]   --->one line code

# how many super over finishes have occured
print(ipl[ipl['SuperOver'] == 'Y'].shape[0])

# how many matches has csk won in kolkata
print(ipl[(ipl['City'] == 'Kolkata') & (ipl['WinningTeam'] == 'Chennai Super Kings')].shape[0])

# toss winner is match winner in percentage
print((ipl[ipl['TossWinner'] == ipl['WinningTeam']].shape[0]/ipl.shape[0])*100)

# movies with rating higher than 8 and votes>10000
print(movies[(movies['imdb_rating'] > 8) & (movies['imdb_votes'] > 10000)].shape[0])

# Action movies with rating higher than 7.5
# mask1 = movies['genres'].str.split('|').apply(lambda x:'Action' in x)
mask1 = movies['genres'].str.contains('Action')
mask2 = movies['imdb_rating'] > 7.5

print(movies[mask1 & mask2])

# Adding new cols
# completely new
movies['Country'] = 'India'
print(movies.head())

# from existing ones
movies.dropna(inplace=True)

movies['lead actor'] = movies['actors'].str.split('|').apply(lambda x:x[0])
print(movies.head())

print(movies.info())

# Important DataFrame Functions

# astype
print(ipl.info())

ipl['ID'] = ipl['ID'].astype('int32')

print(ipl.info())

# ipl['Season'] = ipl['Season'].astype('category')
ipl['Team1'] = ipl['Team1'].astype('category')
ipl['Team2'] = ipl['Team2'].astype('category')

print(ipl.info())