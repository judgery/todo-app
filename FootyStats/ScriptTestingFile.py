import streamlit as st
import pandas as pd
import soccerdata as sd
import polars as pl


# select_league = st.selectbox(
#     "Select League",
#     ["ENG-Premier League",
#     'ESP-La Liga',
#     'FRA-Ligue 1',
#     'GER-Bundesliga',
#     'ITA-Serie A'],
#     index=None
# )
# leagues = select_league

#leagues = ['ENG-Premier League']
seasons = ['2021/2022','2022/2023', '2023/2024', '2024/2025']

select_league = st.radio(
    "Select League",
    ['ENG-Premier League','ESP-La Liga','FRA-Ligue 1','GER-Bundesliga','ITA-Serie A'],
    index=None
)

print(select_league)