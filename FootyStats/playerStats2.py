import streamlit as st
import pandas as pd

select_league = [st.sidebar.selectbox(
    "Select League",
    ['Premier League',
    'La Liga',
    'Ligue 1',
    'Bundesliga',
    'Serie A'],
    index=0,
    width=250
)]

select_season = st.sidebar.selectbox(
    "Select Seasons",
    ['2021/2022','2022/2023','2023/2024','2024/2025'],
    index=0,
    width=250
)

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

df = pd.read_csv("FootyStats/Player_SeasonStats/all_"+season+".csv")

league = ''.join(select_league)
league_df = df[(df['Comp'] == league)]

unique_clubs = league_df['Squad'].unique()
a_unique_clubs = sorted(unique_clubs)

select_team = st.sidebar.selectbox(
    "Select Team",
    a_unique_clubs,
    index=0,
    width=250
)


# unique_players = df['Player'].unique()
# a_unique_players = sorted(unique_players)

club = df[(df['Squad'] == select_team)]
filter_players = club[['Player','Squad','Comp','TCmp','TAtt','TCmp%','Ast','xAG','xA','A-xAG','Matches']]

# select_player = st.sidebar.selectbox(
#     "Select Player",
#     filter_players
# )
#
# overall_df = df[(df['Player'] == select_player)]
# overall = overall_df[['Player','Squad','TCmp','TAtt','TCmp%']]
#
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

