# Pandas Dataframe Function

import numpy as np
import pandas as pd

# value_counts(series and dataframe)
# DataFrame 
marks = pd.DataFrame([
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,70,14],
    [80,70,14]
],columns=['iq','marks','package'])

print(marks)

print(marks.value_counts())

# Series 
a = pd.Series([1,1,1,2,2,3])
print(a.value_counts())

movies = pd.read_csv(r'C:\Users\rajni\OneDrive\Documents\PycharmProjects\RajnishProject\.idea\pandas\movies.csv')
print(movies)

ipl = pd.read_csv(r'C:\Users\rajni\OneDrive\Documents\PycharmProjects\RajnishProject\.idea\pandas\ipl-matches.csv')
print(ipl)

# find which player has won most potm -> in finals and qualifiers
print(ipl[~ipl['MatchNumber'].str.isdigit()]['Player_of_Match'].value_counts())

# Toss decision 
print(ipl['TossDecision'].value_counts())

# how many matches each team has played
print((ipl['Team2'].value_counts() + ipl['Team1'].value_counts()).sort_values(ascending=False))

# sort_values(series and dataframe) -> ascending -> na_position -> inplace -> multiple cols
###############
x = pd.Series([12,14,1,56,89])
print(x)
# ascending order 
print(x.sort_values())
# descending order 
print(x.sort_values(ascending = False))
#####################
print(movies.head(4))

# from a to z 
print(movies.sort_values('title_x'))

# from z to a 
print(movies.sort_values('title_x',ascending = False))
#################
students = pd.DataFrame(
    {
        'name':['nitish','ankit','rupesh',np.nan,'mrityunjay',np.nan,'rishabh',np.nan,'aditya',np.nan],
        'college':['bit','iit','vit',np.nan,np.nan,'vlsi','ssit',np.nan,np.nan,'git'],
        'branch':['eee','it','cse',np.nan,'me','ce','civ','cse','bio',np.nan],
        'cgpa':[6.66,8.25,6.41,np.nan,5.6,9.0,7.4,10,7.4,np.nan],
        'package':[4,5,6,np.nan,6,7,8,9,np.nan,np.nan]

    }
)
print(students)

'''students.sort_values('name',na_position='first',ascending=False,inplace=True)   # na_position for nan value

print(students)'''
###################

print(movies.sort_values(['year_of_release','title_x'],ascending=[True,False]))

# rank(series)
batsman = pd.read_csv(r'C:\Users\rajni\OneDrive\Documents\PycharmProjects\RajnishProject\.idea\pandas\batsman_runs_ipl.csv')
print(batsman.head())

print(batsman['batsman_run'].rank(ascending=False))

batsman['batting_rank'] = batsman['batsman_run'].rank(ascending=False)
print(batsman)
print(batsman.sort_values('batting_rank'))

# sort_index(series and dataframe)   ----> sort the index values

marks = {
    'maths':67,
    'english':57,
    'science':89,
    'hindi':100
}

marks_series = pd.Series(marks)
print(marks_series)

print(marks_series.sort_index(ascending=False))

##################
print(movies.sort_index(ascending=False))

# set_index(dataframe) -> inplace
print(batsman)
batsman.set_index('batter',inplace=True)
print(batsman)

# reset_index(series + dataframe) -> drop parameter
batsman.reset_index(inplace=True)
print(batsman)

# how to replace existing index without loosing
print(batsman.reset_index().set_index('batting_rank'))

# series to dataframe using reset_index
print(marks_series.reset_index())

# rename(dataframe) -> index
movies.set_index('title_x',inplace=True)
print(movies)

movies.rename(columns={'imdb_id':'imdb','poster_path':'link'},inplace=True)
print(movies)

print(movies.rename(index={'Uri: The Surgical Strike':'Uri','Battalion 609':'Battalion'}))

# unique(series)
# nunique(series + dataframe) -> does not count nan
temp = pd.Series([1,1,2,2,3,3,4,4,5,5,np.nan,np.nan])
print(temp)

print(temp.unique())
print(len(temp.unique()))  #count nan value
print(temp.nunique())   # donot count nan value
################
print(ipl['Season'].unique())
print(len(ipl['Season'].unique()))
print(ipl['Season'].nunique())

print(ipl.nunique())

# isnull(series + dataframe)
print(students['name'][students['name'].isnull()])
print(students.isnull())

# notnull(series + dataframe)
print(students['name'][students['name'].notnull()])
print(students.notnull())

# hasnans(series)
print(students['name'].hasnans)

# dropna(series + dataframe) -> how parameter -> works like or
print(students['name'].dropna())

# row 
print(students.dropna(how='any'))

print(students.dropna(how='all'))
# column 
print(students.dropna(subset=['name']))

print(students.dropna(subset=['name','college']))

'''students.dropna(inplace=True)
print(students)'''

# fillna(series + dataframe)
print(students['name'].fillna('unknown'))

print(students)

print(students['package'].fillna(students['package'].mean()))

print(students['name'].fillna(method='ffill'))
print(students['name'].fillna(method='bfill'))

# drop_duplicates(series + dataframe) -> works like and -> duplicated()
temp = pd.Series([1,1,1,2,3,3,4,4])
print(temp)
print(temp.drop_duplicates())
####################
print(marks_series.drop_duplicates(keep='last'))
print(marks_series.drop_duplicates(keep='first'))

# find the last match played by virat kohli in Delhi
ipl['all_players'] = ipl['Team1Players'] + ipl['Team2Players']
print(ipl.head())

def did_kohli_play(players_list):
  return 'V Kohli' in players_list

ipl['did_kohli_play'] = ipl['all_players'].apply(did_kohli_play)
print(ipl[(ipl['City'] == 'Delhi') & (ipl['did_kohli_play'] == True)].drop_duplicates(subset=['City','did_kohli_play'],keep='first'))

##########################
print(students.drop_duplicates())

# drop(series + dataframe)
temp = pd.Series([10,2,3,16,45,78,10])
print(temp)

print(temp.drop(index=[0,6]))

####################
print(students)
students.drop(columns=['branch','cgpa'],inplace=True)
print(students)
print(students.drop(index=[3,4]))

print(students.set_index('name').drop(index=['nitish','aditya']))

# apply(series + dataframe)
temp = pd.Series([10,20,30,40,50])
print(temp)

def sigmoid(value):
  return 1/1+np.exp(-value)

print(temp.apply(sigmoid))
###############
points_df = pd.DataFrame(
    {
        '1st point':[(3,4),(-6,5),(0,0),(-10,1),(4,5)],
        '2nd point':[(-3,4),(0,0),(2,2),(10,10),(1,1)]
    }
)
print(points_df)

def euclidean(row):
  pt_A = row['1st point']
  pt_B = row['2nd point']

  return ((pt_A[0] - pt_B[0])**2 + (pt_A[1] - pt_B[1])**2)**0.5

points_df['distance'] = points_df.apply(euclidean,axis=1)
print(points_df)