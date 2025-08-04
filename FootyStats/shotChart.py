import json
import pandas as pd
import streamlit as st
from mplsoccer import VerticalPitch
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import os

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

with open("FootyStats/TeamStats/"+json_to_open, "r") as file:
    id_data = json.load(file)

n_data = pd.json_normalize(id_data['datesData'])
df = pd.DataFrame(n_data)

unique_id = df['id'].unique()
a_unique_id = sorted(unique_id)

match_folder = "FootyStats/Player_MatchStats/"

teams = set()

for match_id in a_unique_id:
    file_path = os.path.join(match_folder, f"match_{match_id}.json")
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            match_data = json.load(file)
            match_info = match_data.get("match_info", {})
            if "team_h" in match_info:
                teams.add(match_info["team_h"])
            if "team_a" in match_info:
                teams.add(match_info["team_a"])

a_unique_clubs = sorted(teams)

players = set()

for match_id in a_unique_id:
    file_path = os.path.join(match_folder, f"match_{match_id}.json")
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            match_data = json.load(file)
            rosters = match_data.get("rostersData", {})
            for side in ['h', 'a']:
                for player in rosters.get(side, {}).values():
                    if player.get("team_id") and match_data.get("match_info", {}).get(f"team_{side}") == select_team:
                        players.add(player["player"])

a_unique_players = sorted(players)

select_player = st.sidebar.selectbox(
    "Select Player",
    a_unique_players
)
shots_all = []

for match_id in a_unique_id:
    file_path = os.path.join(match_folder, f"match_{match_id}.json")
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            try:
                data = json.load(file)
                shots = data.get("shotsData", {}).get("h", []) + data.get("shotsData", {}).get("a", [])
                for shot in shots:
                    if shot.get("player") == select_player:
                        shots_all.append({
                            "X": float(shot["X"]),
                            "Y": float(shot["Y"]),
                            "xG": float(shot["xG"]),
                            "result": shot["result"]
                        })
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
    else:
        print(f"File not found: {file_path}")

df = pd.DataFrame(shots_all)

pitch = VerticalPitch(pitch_type='statsbomb', half=True, line_color='white', pitch_color='#86bd6d', stripe=False)
fig, ax = pitch.draw(figsize=(8, 5))

if not df.empty:
    df["x"] = df["X"] * 120
    df["y"] = df["Y"] * 80

    result_colour = {
        "Goal": "green",
        "SavedShot": "blue",
        "MissedShots": "red",
        "BlockedShot": "gray"
    }

    df["colour"] = df["result"].map(result_colour).fillna("black")

    pitch.scatter(
        df["x"], df["y"],
        ax=ax,
        s=df["xG"] * 1000,  # scale xG to size
        color=df["colour"],
        edgecolors='black',
        alpha=0.8,
        zorder=2
    )

    # Create legend
    legend_elements = [
        Line2D([0], [0], marker='o', color='w', label='Goal',
               markerfacecolor='green', markeredgecolor='black', markersize=10),
        Line2D([0], [0], marker='o', color='w', label='Saved',
               markerfacecolor='blue', markeredgecolor='black', markersize=10),
        Line2D([0], [0], marker='o', color='w', label='Missed',
               markerfacecolor='red', markeredgecolor='black', markersize=10),
        Line2D([0], [0], marker='o', color='w', label='Blocked',
               markerfacecolor='gray', markeredgecolor='black', markersize=10)
    ]

    ax.legend(handles=legend_elements, loc='lower left', fontsize=10, frameon=True)

ax.set_title(f'{select_player}'f" Shot Map {select_season}", fontsize=16)

st.pyplot(plt.gcf())