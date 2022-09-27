import pandas as pd
import random
import time
from datetime import datetime
  
# All data collected from local .CSV files
df = pd.read_csv('film_collection.csv')
film_collection = df.drop(columns = ['URL', 'Description'])

df2 = pd.read_csv('ext_diary.csv')
diary = df2.drop(columns = ['Date', 'Year', 'Letterboxd URI', 'Rating', 'Tags'])
diary.rename(columns = {'Name': 'Title'}, inplace = True)

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

    # Rest of the function prints out randomized selection from dataset gathered above
    time.sleep(3.0) 

    year_titles_series = film_library[film_library.Year == movie_year].Name
    year_titles = year_titles_series.tolist()

    if len(year_titles) < 1:
        return "I own 0 films from this year."
    else:
        rec_id = random.randint(0, len(year_titles)-1)
        recommendation = year_titles[rec_id]

    return "You should watch '{rec}' tonight!".format(rec = recommendation)

# print(rec_by_year(film_collection))

# Returns most recent date the entered film was watched by the film collection owner
def last_seen(dates_df):
    print()
    film_title = input("Enter a film title: ")
    df_title = ""
    print()
    date_lst = []

    for i in range(len(dates_df)):
        if dates_df.iloc[i]['Title'].lower() == film_title.lower():
            date_lst.append(dates_df.iloc[i]['Watched Date'])
            df_title = dates_df.iloc[i]['Title']
    if not date_lst:
        print("Sorry, you haven't watched this film since you began logging on Letterboxd!")
        return None
    else:
     date_last_seen = date_lst[-1]
    
    ls_split = date_last_seen.split("-")
    last_seen = ls_split[1] + '-' + ls_split[2] + '-' + ls_split[0]

    raw_date = datetime.strptime(last_seen, "%m-%d-%Y")
    date_str = datetime.strftime(raw_date, "%A, %B %d, %Y")

    ago_date = datetime.now() - raw_date
    ago_str = str(ago_date).split(',')
    days_ago = ago_str[0]

    print("You last saw '{film}' on {date}. That was {days} ago.".format(film=df_title, date=date_str, days=days_ago))

    return date_last_seen

# print(last_seen(diary))

print("Hello!")
print("What feature would you like to use?")
print()
print("1. Movie recommendation by year\n2. Last time you saw a particular film")
print()
select_function = input(": ")

if select_function == '1':
    print(rec_by_year(film_collection))
elif select_function == '2':
    print(last_seen(diary))
else:
    print("Sorry, that was not an option!")