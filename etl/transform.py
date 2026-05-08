import pandas as pd

print("Iniciando transformação dos dados...")

# =========================
# SPOTIFY
# =========================

spotify = pd.read_csv("data/raw/spotify_tracks.csv")

spotify.dropna(inplace=True)

spotify['duration_minutes'] = spotify['duration_ms'] / 60000

spotify['duration_minutes'] = spotify['duration_minutes'].round(2)

spotify['platform'] = 'Spotify'

# =========================
# YOUTUBE
# =========================

youtube = pd.read_csv("data/raw/youtube_videos.csv")

youtube.dropna(inplace=True)

youtube['views'] = pd.to_numeric(youtube['views'])

youtube['likes'] = pd.to_numeric(youtube['likes'])

youtube['comments'] = pd.to_numeric(youtube['comments'])

youtube['engagement'] = (
    youtube['likes'] + youtube['comments']
) / youtube['views']

youtube['engagement'] = youtube['engagement'].round(4)

youtube['platform'] = 'YouTube'

# =========================
# SALVAR
# =========================

spotify.to_csv(
    "data/processed/spotify_clean.csv",
    index=False
)

youtube.to_csv(
    "data/processed/youtube_clean.csv",
    index=False
)

print("\nTransformação concluída com sucesso!")

print("\nSpotify:")
print(spotify.head())

print("\nYouTube:")
print(youtube.head())