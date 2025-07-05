import json
import streamlit as st
import pandas as pd
import soccerdata as sd
import polars as pl

# select_league = st.sidebar.selectbox(
#     "Select League",
#     ['ENG-Premier League',
#     'ESP-La Liga',
#     'FRA-Ligue 1',
#     'GER-Bundesliga',
#     'ITA-Serie A'],
#     index=0,
#     width=250
# )
# select_season = st.sidebar.selectbox(
#     "Select Seasons",
#     ['2021/2022','2022/2023','2023/2024','2024/2025'],
#     index=0,
#     width=250
# )
#
# if select_league == 'ENG-Premier League':
#     league = 'EPL'
# if select_league == 'ESP-La Liga':
#     league = 'LaLiga'
# if select_league == 'FRA-Ligue 1':
#     league = 'Ligue1'
# if select_league == 'GER-Bundesliga':
#     league = 'Bundesliga'
# if select_league == 'ITA-Serie A':
#     league = 'SerieA'
# else:
#     print(f'Select League')
#
# if select_season == '2021/2022':
#     season = '2021'
# if select_season == '2022/2023':
#     season = '2022'
# if select_season == '2023/2024':
#     season = '2023'
# if select_season == '2024/2025':
#     season = '2024'
# else:
#     print(f'Select Season')

league = 'EPL'
season = '2024'

json_to_open = league+"_"+season+".json"

# with open("FootyStats/TeamStats/"+json_to_open) as json_file:
#     data = json.loads(json_file.read())
#     #print(data)

with open("TeamStats/"+json_to_open) as json_file:
    data = json.load(json_file)

# Normalise JSON data
n_data = pd.json_normalize(data['datesData'])
df = pd.DataFrame(n_data)

#print(xG_h)

team_selection = 'Manchester United'

# Print results
club = df[(df['h.title'] == team_selection) | (df['a.title'] == team_selection)]
club_results = club[['h.title','goals.h','goals.a','a.title','datetime']]
#print(club_results)

# Filter unique club names for dropdown & order
unique_clubs = df['h.title'].unique()
a_unique_clubs = sorted(unique_clubs)
#print(a_unique_clubs)

# Calculate home xG based on team_selection variable