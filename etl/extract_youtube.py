from googleapiclient.discovery import build
from dotenv import load_dotenv
import os
import pandas as pd

print("Extraindo dados do YouTube...")

load_dotenv()

api_key = os.getenv("YOUTUBE_API_KEY")

youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.videos().list(
    part="snippet,statistics",
    chart="mostPopular",
    regionCode="BR",
    maxResults=20
)

response = request.execute()

videos = []

for item in response['items']:

    videos.append({
        'title': item['snippet']['title'],
        'channel': item['snippet']['channelTitle'],
        'views': item['statistics'].get('viewCount', 0),
        'likes': item['statistics'].get('likeCount', 0),
        'comments': item['statistics'].get('commentCount', 0)
    })

df = pd.DataFrame(videos)

df.to_csv("data/raw/youtube_videos.csv", index=False)

print("\nDados salvos em:")
print("data/raw/youtube_videos.csv")
print("\nPrimeiros vídeos:")
print(df.head())