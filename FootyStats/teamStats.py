import json
import streamlit as st
import pandas as pd
import soccerdata as sd
import polars as pl
import math


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

st.title("Season Results")
st.dataframe(
    club_results,
    width=550,
    column_config={
        "h.title": "Home Team",
        "goals.h": "",
        "goals.a": "",
        "a.title": "Away Team",
        "datetime": "Date/Time"
    },
    hide_index=True
)


club = df[(df['h.title'] == select_team)]
club_h_xG = club['xG.h'].astype(float)
club_h_xG_sum = math.fsum(club_h_xG).__round__(2)

club = df[(df['a.title'] == select_team)]
club_a_xG = club['xG.a'].astype(float)
club_a_xG_sum = math.fsum(club_a_xG).__round__(2)

club_c_xG_sum = math.fsum([club_h_xG_sum, club_a_xG_sum]).__round__(2)

club = df[(df['h.title'] == select_team)]
club_h_goals = club['goals.h'].astype(float)
club_h_goals_sum = math.fsum(club_h_goals).__round__(0)

club = df[(df['a.title'] == select_team)]
club_a_goals = club['goals.a'].astype(float)
club_a_goals_sum = math.fsum(club_a_goals)

club_c_goals_sum = sum((club_h_goals_sum, club_a_goals_sum)).__round__(0)



col1, col2, col3 = st.columns(3)

with col1:
    st.header("Home Goals", divider="green")
    st.subheader(int(club_h_goals_sum))

with col2:
    st.header("Away Goals", divider="green")
    st.subheader(int(club_a_goals_sum))

with col3:
    st.header("Total Goals", divider="green")
    st.subheader(int(club_c_goals_sum))


col4, col5, col6 = st.columns(3)

with col4:
    st.header("xG Home", divider="green")
    st.subheader(club_h_xG_sum)

with col5:
    st.header("xG Away", divider="green")
    st.subheader(club_a_xG_sum)

with col6:
    st.header("xG Total", divider="green")
    st.subheader(club_c_xG_sum)



#
#
# st.write(f"Home xG: ")
# st.markdown(club_h_xG_sum)
# st.write(f"Away xG")
# st.markdown(club_a_xG_sum)
# st.write(f"Total xG")
# st.markdown(club_c_xG_sum)