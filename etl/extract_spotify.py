import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os
import pandas as pd

print("Extraindo dados do Spotify...")

load_dotenv()

client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

auth_manager = SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret
)

sp = spotipy.Spotify(auth_manager=auth_manager)

results = sp.search(
    q='Taylor Swift',
    type='track'
)

tracks = []

for item in results['tracks']['items']:

    tracks.append({
    'music_name': item.get('name'),
    'artist': item['artists'][0]['name'],
    'popularity': item.get('popularity', 50),
    'duration_ms': item.get('duration_ms', 0)
})

df = pd.DataFrame(tracks)

df.to_csv("data/raw/spotify_tracks.csv", index=False)

print("\nDados salvos com sucesso!")
print("\nPrimeiras músicas:")
print(df.head())