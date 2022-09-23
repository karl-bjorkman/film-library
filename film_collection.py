import pandas as pd
import random
import time

# All data collected from local .CSV files
df = pd.read_csv('film_collection.csv')
film_collection = df.drop(columns = ['URL', 'Description'])

df2 = pd.read_csv('ext_diary.csv')
diary = df2.drop(columns=['Date', 'Year', 'Letterboxd URI', 'Rating', 'Tags'])
diary.rename(columns={'Name': 'Title'}, inplace=True)

# Returns a randomized film recommendation from the inputted year
def rec_by_year(film_library):
    rec_id = 0
    recommendation = ''

    print()
    movie_year = int(input("Enter a movie year: "))
    year_titles_db = film_library[film_library.Year == movie_year]

    print()
    print(year_titles_db)
    print()

    time.sleep(2.0)

    year_titles_series = film_library[film_library.Year == movie_year].Name
    year_titles = year_titles_series.tolist()

    if len(year_titles) < 1:
        return "I own 0 films from this year."
    else:
        rec_id = random.randint(0, len(year_titles)-1)
        recommendation = year_titles[rec_id]

    return "You should watch '{rec}' tonight!".format(rec = recommendation)

print(rec_by_year(film_collection))

# Returns most recent date the inputted film was watched by the user
def last_seen(dates_df):
    print()
    film_title = input("Enter a film title: ")
    date_lst = []

    for i in range(len(dates_df)):
        if dates_df.iloc[i]['Title'] == film_title:
            date_lst.append(dates_df.iloc[i]['Watched Date'])
    date_last_seen = date_lst[-1]

    return "You last saw '{film}' on {date}.".format(film=film_title, date=date_last_seen)

print(last_seen(diary))