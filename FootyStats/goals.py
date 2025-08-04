import streamlit as st
import pandas as pd
import json

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

min_goals = int(st.sidebar.text_input("Enter minimum number of goals", 10))
num_of_results = int(st.sidebar.text_input("Enter number of results", 10))

with open("./FootyStats/TeamStats/"+json_to_open) as json_file:
    data = json.load(json_file)

players_list = []

for player in data["playersData"]:
    player_name = player.get("player_name", "Unknown")
    team_title = player.get("team_title")
    goals = float(player.get("goals", 0.0))
    xG = float(player.get("xG", 0.0))
    shots = float(player.get("shots", 0.0))

    players_list.append({
        "Player": player_name,
        "Team": team_title,
        "Goals": goals,
        "xG": xG,
        "Shots": shots
    })

df_shots = pd.DataFrame(players_list)

df_shots['xG'] = df_shots['xG'].round(2)
df_shots['G to xG'] = df_shots['Goals'] / df_shots['xG']
df_shots['xG per shot'] = df_shots['xG'] / df_shots['Shots']


goals_df = df_shots.loc[df_shots["Goals"] >= min_goals]
xg_df = df_shots.loc[df_shots["Goals"] >= min_goals].sort_values("G to xG", ascending=False)
xg_df_asc = df_shots.loc[df_shots["Goals"] >= min_goals].sort_values("G to xG", ascending=True)


df_topscorers=pd.DataFrame(
    goals_df
    .sort_values(by=["Goals", "G to xG"],ascending=False)
    .head(num_of_results)
)

df_bestxg = pd.DataFrame(
    xg_df
    .head(num_of_results)[df_shots.Goals>= min_goals]
    .sort_values("G to xG", ascending=False)
)

df_worstxg = pd.DataFrame(
    xg_df_asc
    .head(num_of_results)[df_shots.Goals>= min_goals]
    .sort_values("G to xG", ascending=True)
)

st.subheader("Top Scorers")
st.dataframe(
    df_topscorers,
    hide_index=True
)

st.subheader("Best Goal / xG Ratio")
st.dataframe(
    df_bestxg,
    hide_index=True
)

st.subheader("Worst Goal / xG Ratio")
st.dataframe(
    df_worstxg,
    hide_index=True
)
