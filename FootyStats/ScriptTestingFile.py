# import json
# import streamlit as st
# import pandas as pd
# import soccerdata as sd
# import polars as pl
# import math
# import os

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

# league = 'EPL'
# season = '2024'
#
# json_to_open = league+"_"+season+".json"

# with open("FootyStats/TeamStats/"+json_to_open) as json_file:
#     data = json.loads(json_file.read())
#     #print(data)

# with open("TeamStats/"+json_to_open) as json_file:
#     data = json.load(json_file)

# Normalise JSON data
# n_data = pd.json_normalize(data['datesData'])
# df = pd.DataFrame(n_data)

#print(xG_h)

# team_selection = 'Manchester United'

# Print results
# club = df[(df['h.title'] == team_selection) | (df['a.title'] == team_selection)]
# club_results = club[['h.title','goals.h','goals.a','a.title','datetime']]
#print(club_results)

# Filter unique club names for dropdown & order
# unique_clubs = df['h.title'].unique()
# a_unique_clubs = sorted(unique_clubs)
#print(a_unique_clubs)

# Calculate xG

# Sum xG based on home/away status and combined
# club = df[(df['h.title'] == team_selection)]
# club_h_xG = club['xG.h'].astype(float)
# club_h_xG_sum = math.fsum(club_h_xG)
# print(club_h_xG_sum)

# club = df[(df['a.title'] == team_selection)]
# club_a_xG = club['xG.a'].astype(float)
# club_a_xG_sum = math.fsum(club_a_xG)
# print(club_a_xG_sum)

# club_c_xG_sum = math.fsum([club_h_xG_sum, club_a_xG_sum])
# print(club_c_xG_sum)


# Calculate H/A/C goals similar to xG

# club = df[(df['h.title'] == team_selection)]
# club_h_goals = club['goals.h'].astype(float)
# club_h_goals_sum = math.fsum(club_h_goals)
# print(club_h_goals_sum)

# club = df[(df['a.title'] == team_selection)]
# club_a_goals = club['goals.a'].astype(float)
# club_a_goals_sum = math.fsum(club_a_goals)
# print(club_a_goals_sum)

# club_c_goals_sum = sum((club_h_goals_sum, club_a_goals_sum))
# print(club_c_goals_sum)


# def read_with_bs(path):
#     with open(path, 'r', encoding='utf-8') as f:
#         soup = BeautifulSoup(f, 'lxml')
#     tables = pd.read_html(str(soup))
#     return tables[0]
#
# path = 'Player_SeasonStats/players_ENG-Premier League_2425_passing.html'
# df = read_with_bs(path)
# print(df)


# df = pd.read_csv("Player_SeasonStats/all_2024.csv")
#
# unique_clubs = df['Squad'].unique()
# a_unique_clubs = sorted(unique_clubs)


# select_team = st.sidebar.selectbox(
#     "Select Team",
#     pd.unique(df['Squad']),
#     index=0
# )

# club_df = df[(df['Squad'] == 'Manchester Utd')]
# club_df.sort('Squad')
#print(club_df)

# st.dataframe(club_df,
#              hide_index=True,
#              column_order=["Player",
#                             "Squad",
#                             "TCmp",
#                             "TAtt",
#                             "TCmp%"],
#              column_config={"Player":("Player"),
#                             "Squad":("Team"),
#                             "TCmp":("Total Completed"),
#                             "TAtt":("Total Attempted"),
#                             "TCmp%":("Completed %")
#                             }
#              )
#


# with open("TeamStats/EPL_2024.json", "r") as file:
#     id_data = json.load(file)
#
# n_data = pd.json_normalize(id_data['datesData'])
# df = pd.DataFrame(n_data)
#
# unique_id = df['id'].unique()
# a_unique_id = sorted(unique_id)


# Folder where the JSON files are located
# match_folder = "Player_MatchStats/"

# Initialize list to store Bruno Fernandes's shots
# shots_all = []

# Loop through the list of IDs
# for match_id in a_unique_id:
#     file_path = os.path.join(match_folder, f"match_{match_id}.json")
#     if os.path.exists(file_path):
#         with open(file_path, "r") as file:
#             try:
#                 data = json.load(file)
#                 shots = data.get("shotsData", {}).get("h", []) + data.get("shotsData", {}).get("a", [])
#                 for shot in shots:
#                     if shot.get("player") == "Bruno Fernandes":
#                         shots_all.append({
#                             "X": float(shot["X"]),
#                             "Y": float(shot["Y"]),
#                             "xG": float(shot["xG"]),
#                             "result": shot["result"]
#                         })
#             except Exception as e:
#                 print(f"Error reading {file_path}: {e}")
#     else:
#         print(f"File not found: {file_path}")
#
# # Create a combined DataFrame
# df = pd.DataFrame(shots_all)
#
# print(f"Collected {len(df)} shots from {len(a_unique_id)} matches.")
# print(df)

import json
import pandas as pd

with open("TeamStats/EPL_2024.json", "r") as file:
    data = json.load(file)

players_list = []

for player in data["playersData"]:
    player_name = player.get("player_name", "Unknown")
    goals = float(player.get("goals", 0.0))
    xG = float(player.get("xG", 0.0))
    shots = float(player.get("shots", 0.0))

    players_list.append({
        "Player": player_name,
        "Goals": goals,
        "xG": xG,
        "Shots": shots
    })

df_shots = pd.DataFrame(players_list)

df_shots['xG'] = df_shots['xG'].round(2)
df_shots['xG_G'] = df_shots['Goals'] / df_shots['xG']
df_shots['xG_shot'] = df_shots['xG'] / df_shots['Shots']

print(df_shots.head())