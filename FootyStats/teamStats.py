import json
import streamlit as st
import pandas as pd
import math


select_league = st.sidebar.selectbox(
    "Select League",
    ['Premier League',
    'La Liga',
    'Ligue 1',
    'Bundesliga',
    'Serie A'],
    index=0,
    width=250
)
select_season = st.sidebar.selectbox(
    "Select Seasons",
    ['2021/2022','2022/2023','2023/2024','2024/2025'],
    index=0,
    width=250
)

if select_league == 'Premier League':
    league = 'EPL'
if select_league == 'La Liga':
    league = 'LaLiga'
if select_league == 'Ligue 1':
    league = 'Ligue1'
if select_league == 'Bundesliga':
    league = 'Bundesliga'
if select_league == 'Serie A':
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

df = pd.read_csv("FootyStats/Player_SeasonStats/all_"+season+".csv")

league = ''.join(select_league)
league_df = df[(df['Comp'] == league)]

unique_clubs = league_df['Squad'].unique()
a_unique_clubs = sorted(unique_clubs)


club = df[(df['Squad'] == select_team)]
filter_players = club[['Player','Squad','Comp','TCmp','TAtt','TCmp%','Ast','xAG','xA','A-xAG','Matches']]

st.markdown("###")
st.subheader("Team Passing Stats")
st.dataframe(filter_players,
             hide_index=True,
             column_order=["Player",
                            "Squad",
                            "TCmp",
                            "TAtt",
                            "TCmp%"],
             column_config={"Player":("Player"),
                            "Squad":("Team"),
                            "TCmp":("Total Completed"),
                            "TAtt":("Total Attempted"),
                            "TCmp%":("Completed %")
                            }
             )

st.markdown("###")
st.subheader("Team Assist Stats")
st.dataframe(filter_players,
             hide_index=True,
             column_order=["Player",
                           "Squad",
                           "Ast",
                           "xAG",
                           "xA",
                           "A-xAG"],
             column_config={"Player":("Player"),
                            "Squad":("Team"),
                            "Ast":("Assists"),
                            "xAG":("xAssist-Goal"),
                            "xA%":("xAssist %"),
                            "A-xAG":("Assist/xAssist")
                            }
             )

