import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("netflix_titles.csv")

print("\nDataset information:\n")
print(df.info())

print("\nShape of the dataset:\n")
print(df.shape)

print("\nData types of columns :\n")
print(df.dtypes)

print("\nTop 5 values from data:\n")
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
print(df.head())

print("\nMissing values before cleaning:\n")
print(df.isnull().sum())

print("\nDuplicated values:\n")
print(df.duplicated().sum())

print("\nDuplicated show id:\n")
print(df['show_id'].duplicated().sum())


# STEP 1: Handle missing values
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')
df['country'] = df['country'].fillna('Unknown')
df['date_added'] = df['date_added'].fillna('Unknown')
df['rating'] = df['rating'].fillna('Unknown')
df['duration'] = df['duration'].fillna('Unknown')

print("\nMissing values after cleaning:\n")
print(df.isnull().sum())

print("\n Graphical representation :\n")

df['type'].value_counts().plot(kind='bar')

plt.title('Movies vs TV Shows on Netflix')
plt.xlabel('Type')
plt.ylabel('Number of Titles')
plt.show()


# ============================================================
# NETFLIX DATA ANALYSIS
# ============================================================

# ANALYSIS 1: Movies vs TV Shows - Pie Chart
type_count = df['type'].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(type_count.values, labels=type_count.index, autopct='%1.1f%%', startangle=90)
plt.title('Movies vs TV Shows on Netflix')
plt.show()

# ANALYSIS 2: Content by Release Year - Line Chart
year_count = df['release_year'].value_counts().sort_index()

plt.figure(figsize=(12, 5))
plt.plot(year_count.index, year_count.values)
plt.title('Netflix Content by Release Year')
plt.xlabel('Release Year')
plt.ylabel('Number of Titles')
plt.grid()
plt.show()

# ANALYSIS 3: Top 10 Countries - Horizontal Bar Chart
country_count = df['country'].value_counts().head(10).sort_values()

plt.figure(figsize=(10, 6))
plt.barh(country_count.index, country_count.values)
plt.title('Top 10 Countries Producing Netflix Content')
plt.xlabel('Number of Titles')
plt.ylabel('Country')
plt.show()

# ANALYSIS 4: Top 10 Content Ratings - Bar Chart
rating_count = df['rating'].value_counts().head(10)

plt.figure(figsize=(10, 5))
plt.bar(rating_count.index, rating_count.values)
plt.title('Top Netflix Content Ratings')
plt.xlabel('Rating')
plt.ylabel('Number of Titles')
plt.show()

# ANALYSIS 5: Top 10 Genres - Horizontal Bar Chart
genres = df['listed_in'].dropna().str.split(', ')
genre_count = {}

for genre_list in genres:
    for genre in genre_list:
        genre_count[genre] = genre_count.get(genre, 0) + 1

genre_series = pd.Series(genre_count).sort_values(ascending=True).tail(10)

plt.figure(figsize=(10, 6))
plt.barh(genre_series.index, genre_series.values)
plt.title('Top 10 Genres on Netflix')
plt.xlabel('Number of Titles')
plt.ylabel('Genre')
plt.show()

# ANALYSIS 6: Movies vs TV Shows Over the Years - Line Chart
movie_year = (
    df[df['type'] == 'Movie']['release_year']
    .value_counts()
    .sort_index()
)

tv_year = (
    df[df['type'] == 'TV Show']['release_year']
    .value_counts()
    .sort_index()
)

plt.figure(figsize=(12, 5))
plt.plot(movie_year.index, movie_year.values, label='Movies')
plt.plot(tv_year.index, tv_year.values, label='TV Shows')
plt.title('Movies vs TV Shows Over the Years')
plt.xlabel('Release Year')
plt.ylabel('Number of Titles')
plt.legend()
plt.grid()
plt.show()

# ANALYSIS 7: Movie Duration Distribution - Histogram
movies = df[df['type'] == 'Movie'].copy()

# Convert duration into numeric minutes
movies['duration_minutes'] = (
    movies['duration']
    .str.replace(' min', '', regex=False)
)

movies['duration_minutes'] = pd.to_numeric(
    movies['duration_minutes'], errors='coerce'
)

plt.figure(figsize=(10, 5))
plt.hist(movies['duration_minutes'].dropna(), bins=20)
plt.title('Distribution of Movie Durations')
plt.xlabel('Duration (Minutes)')
plt.ylabel('Number of Movies')
plt.show()

average_duration = movies['duration_minutes'].mean()
print('Average Movie Duration:', round(average_duration, 2), 'minutes')

# ANALYSIS 8: Top 10 Directors - Horizontal Bar Chart
director_count = (
    df[df['director'] != 'Unknown']['director']
    .value_counts()
    .head(10)
    .sort_values()
)

plt.figure(figsize=(10, 6))
plt.barh(director_count.index, director_count.values)
plt.title('Top 10 Directors on Netflix')
plt.xlabel('Number of Titles')
plt.ylabel('Director')
plt.show()

print('All 8 Netflix analyses completed successfully.')
