from sqlalchemy import create_engine
import pandas as pd

print("Carregando dados para PostgreSQL...")

engine = create_engine(
    "postgresql://postgres:723541@localhost:5432/music_analysis"
)

spotify = pd.read_csv(
    "data/processed/spotify_clean.csv"
)

youtube = pd.read_csv(
    "data/processed/youtube_clean.csv"
)

spotify.to_sql(
    "spotify_tracks",
    engine,
    if_exists="replace",
    index=False
)

youtube.to_sql(
    "youtube_videos",
    engine,
    if_exists="replace",
    index=False
)

print("\nDados carregados com sucesso!")