import pandas as pd
import random
import time

df = pd.read_csv('film_collection.csv')
df2 = pd.read_csv('ratings.csv')
film_collection = df.drop(columns=['URL', 'Description'])
ratings = df2.drop(columns = ['Letterboxd URI'])

# updated_films_csv = film_collection.to_csv('/Users/karlbjorkman/desktop/updated_film_collection.csv')

# year_count = film_collection\
#     .groupby('Year')\
#     ['Position']\
#     .count()\
#     .reset_index()

# year_count.rename(columns = {'Position': 'Count'}, inplace = True)

# print(year_count)

# This code block asks the user for a year and outputs the films from that year that he owns
# def year_titles(film_library):
#     movie_year = int(input("Enter a movie year: "))
#     year_titles = film_library[film_library.Year == movie_year]
#     if year_titles.empty:
#         return "I own 0 films from this year."
#     else:
#         return year_titles

# print(ratings)

def rec_by_year(film_library):
    rec_id = 0
    recommendation = ''

    movie_year = int(input("Enter a movie year: "))
    year_titles_db = film_library[film_library.Year == movie_year]

    print()
    print(year_titles_db)
    print()

    time.sleep(3.0)

    year_titles_series = film_library[film_library.Year == movie_year].Name
    year_titles = year_titles_series.tolist()

    if len(year_titles) < 1:
        return "I own 0 films from this year."
    else:
        rec_id = random.randint(0, len(year_titles)-1)
        recommendation = year_titles[rec_id]

    return "You should watch '{rec}' tonight!".format(rec = recommendation)


print(rec_by_year(film_collection))