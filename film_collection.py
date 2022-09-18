import pandas as pd

df = pd.read_csv('/Users/karlbjorkman/desktop/personal_projects/film_library/film_collection.csv')
film_collection = df.drop(columns = ['URL', 'Description'])
# print(film_collection.head(5))
# print()

# updated_films_csv = film_collection.to_csv('/Users/karlbjorkman/desktop/updated_film_collection.csv')

year_count = film_collection\
    .groupby('Year')\
    ['Position']\
    .count()\
    .reset_index()

year_count.rename(columns = {'Position': 'Count'}, inplace = True)

# print(year_count)

movie_year = int(input("Enter a movie year: "))

def year_titles(film_year):
    year_titles = film_collection[film_collection.Year == film_year]
    if year_titles.empty:
        return "I own 0 films from this year."
    else:
        return year_titles

print(year_titles(movie_year))