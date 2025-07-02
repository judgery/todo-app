import streamlit as st
import pandas as pd
import soccerdata as sd
import polars as pl


select_league = [st.selectbox(
    "Select League",
    ["ENG-Premier League",
    'ESP-La Liga',
    'FRA-Ligue 1',
    'GER-Bundesliga',
    'ITA-Serie A'],
    index=None
)]
leagues = select_league



#leagues = ['ENG-Premier League']
seasons = ['2021/2022','2022/2023', '2023/2024', '2024/2025']

dfs_shots = []
for season in seasons:
    for league in leagues:
        understat = sd.Understat(leagues=league, seasons=season)
        df_shots = understat.read_shot_events()
        df_shots = pl.from_pandas(df_shots, include_index=True)
        df_shots = df_shots.with_columns([
            pl.lit(league).alias("league"),
            pl.lit(season).alias("season")
            ])
        dfs_shots.append(df_shots)

col_order_shots = []
for df in dfs_shots:
    for c in df.columns:
        if c not in col_order_shots:
            col_order_shots.append(c)

aligned_shots = []
for df in dfs_shots:
    missing = [c for c in col_order_shots if c not in df.columns]
    if missing:
        df = df.with_columns([pl.lit(None).alias(c) for c in missing])
    aligned_shots.append(df.select(col_order_shots))

shot_events = pl.concat(aligned_shots, how="vertical")

(
    shot_events
    .with_columns(
        (pl.col("result") == "Goal").alias("goal"))
    .select(
        pl.col("xg").sum().alias("xg_total"),
        pl.col("goal").sum().alias("goals_total"),
        pl.col("shot_id").count().alias("shots_total"))
    .with_columns(
        (pl.col("goals_total")/pl.col("xg_total")).alias("goals_to_xg"),
        (pl.col("xg_total")/pl.col("shots_total")).alias("xg_per_shot"))
)

df_shots = (
    shot_events
    .with_columns(
        (pl.col("result") == "Goal").alias("goal"))
    .group_by(["player"])
    .agg(
        pl.col("xg").sum().alias("xg_total"),
        pl.col("goal").sum().alias("goals_total"),
        pl.col("shot_id").count().alias("shots_total"))
    .with_columns(
        (pl.col("goals_total")/pl.col("xg_total")).alias("goals_to_xg"),
        (pl.col("xg_total")/pl.col("shots_total")).alias("xg_per_shot"))
)

# Top Scorers
df_topscorers=pd.DataFrame(
    df_shots
    .filter(pl.col("goals_total") > 20)
    .sort("goals_total", descending=True)
    .head(30)
)


# Best Goal / xG ratio
df=pd.DataFrame(
    df_shots
    .filter(pl.col("goals_total") > 20)
    .sort("goals_to_xg", descending=True)
    .head(30)

)

st.subheader("Top Scorers")

st.dataframe(
    df_topscorers,
    column_config={
        "0": "Player",
        "1": "xG Total",
        "2": "Total Goals",
        "3": "Total Shots",
        "4": "Goals to xG Ratio",
        "5": "xG per Shot"
    },
    hide_index=True
)

st.subheader("Best Goal / xG Ratio")

st.dataframe(
    df,
    column_config={
        "0": "Player",
        "1": "xG Total",
        "2": "Total Goals",
        "3": "Total Shots",
        "4": "Goals to xG Ratio",
        "5": "xG per Shot"
    },
    hide_index=True
)


