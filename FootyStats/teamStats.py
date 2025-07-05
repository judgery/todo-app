import json
import streamlit as st
import pandas as pd
import soccerdata as sd
import polars as pl


select_league = st.sidebar.selectbox(
    "Select League",
    ['ENG-Premier League',
    'ESP-La Liga',
    'FRA-Ligue 1',
    'GER-Bundesliga',
    'ITA-Serie A'],
    index=0,
    width=250
)
select_season = st.sidebar.selectbox(
    "Select Seasons",
    ['2021/2022','2022/2023','2023/2024','2024/2025'],
    index=0,
    width=250
)

if select_league == 'ENG-Premier League':
    league = 'EPL'
if select_league == 'ESP-La Liga':
    league = 'LaLiga'
if select_league == 'FRA-Ligue 1':
    league = 'Ligue1'
if select_league == 'GER-Bundesliga':
    league = 'Bundesliga'
if select_league == 'ITA-Serie A':
    league = 'SerieA'
else:
    pass

if select_season == '2021/2022':
    season = '2021'
if select_season == '2022/2023':
    season = '2022'
if select_season == '2023/2024':
    season = '2023'
if select_season == '2024/2025':
    season = '2024'
else:
    pass

json_to_open = league+"_"+season+".json"

with open("FootyStats/TeamStats/"+json_to_open) as json_file:
    data = json.load(json_file)

n_data = pd.json_normalize(data['datesData'])
df = pd.DataFrame(n_data)

unique_clubs = df['h.title'].unique()
a_unique_clubs = sorted(unique_clubs)

select_team = st.sidebar.selectbox(
    "Select Team",
    a_unique_clubs,
    index=0,
    width=250
)

club = df[(df['h.title'] == select_team) | (df['a.title'] == select_team)]
club_results = club[['h.title','goals.h','goals.a','a.title','datetime']]

st.subheader("Season Results")
st.dataframe(
    club_results,
    column_config={
        "h.title": "Home Team",
        "goals.h": "",
        "goals.a": "",
        "a.title": "Away Team",
        "datetime": "Date/Time"
    },
    hide_index=True
)

