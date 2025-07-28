import json
import pandas as pd
import streamlit as st
from mplsoccer import VerticalPitch
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import os

# Select league

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

# Select season

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

# Open JSON based on above variables

json_to_open = league+"_"+season+".json"

with open("FootyStats/TeamStats/"+json_to_open) as json_file:
    data = json.load(json_file)

n_data = pd.json_normalize(data['datesData'])
df = pd.DataFrame(n_data)

unique_clubs = df['h.title'].unique()
a_unique_clubs = sorted(unique_clubs)

# Select unique team from list created above
select_team = st.sidebar.selectbox(
    "Select Team",
    a_unique_clubs,
    index=0,
    width=250
)

dfPlayer = pd.read_csv("FootyStats/Player_SeasonStats/all_"+season+".csv")

unique_players = dfPlayer['Player'].unique()
a_unique_players = sorted(unique_players)

club = dfPlayer[(dfPlayer['Squad'] == select_team)]
filter_players = club[['Player']]

select_player = st.sidebar.selectbox(
    "Select Player",
    filter_players
)

getIDjson = league+"_"+season+".json"

with open("FootyStats/TeamStats/"+getIDjson, "r") as file:
    id_data = json.load(file)

n_data = pd.json_normalize(id_data['datesData'])
df = pd.DataFrame(n_data)

unique_id = df['id'].unique()
a_unique_id = sorted(unique_id)

match_folder = "FootyStats/Player_MatchStats/"

shots_all = []

# Loop through the list of IDs
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

# Convert coordinates for UEFA pitch
df["x"] = df["X"] * 105
df["y"] = df["Y"] * 65

result_colour = {
    "Goal": "green",
    "SavedShot": "blue",
    "MissedShots": "red",
    "BlockedShot": "gray"
}

df["color"] = df["result"].map(result_colour).fillna("black")

# Create pitch
pitch = VerticalPitch(pitch_type='uefa', half=True, line_color='white', pitch_color='grass', stripe=True)
fig, ax = pitch.draw(figsize=(8, 5))

# Plot shots
pitch.scatter(
    df["x"], df["y"],
    ax=ax,
    s=df["xG"] * 1000,  # scale xG to size
    color=df["color"],
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

ax.set_title(f'{select_player}'" Shot Map", fontsize=16)

plt.show()