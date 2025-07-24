import pandas as pd
import streamlit as st
import polars as pl

df = pd.read_csv("FootyStats/Player_SeasonStats/all_2024.csv")

unique_clubs = df['Squad'].unique()
a_unique_clubs = sorted(unique_clubs)

unique_players = df['Player'].unique()
a_unique_players = sorted(unique_players)

select_team = st.sidebar.selectbox(
    "Select Team",
    a_unique_clubs,
    index=0
)

club = df[(df['Squad'] == select_team)]
filter_players = club[['Player','Squad','Comp','TCmp','TAtt','TCmp%']]

select_player = st.sidebar.selectbox(
    "Select Player",
    filter_players
)

overall_df = df[(df['Player'] == select_player)]
overall = overall_df[['Player','Squad','TCmp','TAtt','TCmp%']]

st.dataframe(overall,
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
