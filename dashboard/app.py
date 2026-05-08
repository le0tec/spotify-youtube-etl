import streamlit as st
import pandas as pd
import plotly.express as px


st.title("🎵 Spotify & YouTube Trend Analytics")

st.markdown("""
### Dashboard interativo para análise de tendências musicais e audiovisuais
""")


spotify = pd.read_csv(
    "data/processed/spotify_clean.csv"
)

youtube = pd.read_csv(
    "data/processed/youtube_clean.csv"
)


st.sidebar.title("🎛️ Filtros")

top_n = st.sidebar.slider(
    "Quantidade de registros",
    5,
    20,
    10
)

avg_popularity = spotify['popularity'].mean()

total_views = youtube['views'].sum()

avg_engagement = youtube['engagement'].mean()

top_music = spotify.sort_values(
    by="popularity",
    ascending=False
).iloc[0]['music_name']

top_video = youtube.sort_values(
    by="views",
    ascending=False
).iloc[0]['title']

total_likes = youtube['likes'].sum()

col1, col2, col3 = st.columns(3)

col1.metric(
    "🎧 Spotify",
    len(spotify)
)

col2.metric(
    "📺 Views do YouTube",
    f"{total_views:,}"
)

col3.metric(
    "🔥 Engajamento",
    round(avg_engagement, 4)
)

st.markdown("---")

st.success(f"🎵 Música destaque: {top_music}")

st.info(f"📺 Vídeo destaque: {top_video}")

st.warning(f"👍 Total de likes: {total_likes:,}")

st.subheader("🎶 Top músicas mais populares")

spotify_top = spotify.sort_values(
    by="popularity",
    ascending=False
).head(top_n)

fig_spotify = px.bar(
    spotify_top,
    x="music_name",
    y="popularity",
    color="artist",
    text="popularity"
)

fig_spotify.update_layout(
    xaxis_title="Música",
    yaxis_title="Popularidade",
    template="plotly_dark"
)

st.plotly_chart(
    fig_spotify,
    use_container_width=True
)


st.subheader("📹 Vídeos mais visualizados")

youtube_top = youtube.sort_values(
    by="views",
    ascending=False
).head(top_n)

fig_youtube = px.bar(
    youtube_top,
    x="title",
    y="views",
    color="channel",
    text="views"
)

fig_youtube.update_layout(
    xaxis_title="Vídeo",
    yaxis_title="Visualizações",
    template="plotly_dark"
)

st.plotly_chart(
    fig_youtube,
    use_container_width=True
)


st.subheader("🔥 Ranking de Engajamento")

fig_engagement = px.scatter(
    youtube,
    x="views",
    y="engagement",
    size="likes",
    color="channel",
    hover_name="title"
)

fig_engagement.update_layout(
    template="plotly_dark"
)

st.plotly_chart(
    fig_engagement,
    use_container_width=True
)

st.markdown("---")

st.subheader("🏆 Ranking Top 5 Spotify")

st.table(
    spotify_top[
        ['music_name', 'artist', 'popularity']
    ].head(5)
)

st.subheader("🏆 Ranking Top 5 YouTube")

st.table(
    youtube_top[
        ['title', 'channel', 'views']
    ].head(5)
)

st.subheader("📋 Dados Spotify")

st.dataframe(
    spotify,
    use_container_width=True
)

st.subheader("📋 Dados YouTube")

st.dataframe(
    youtube,
    use_container_width=True
)


st.markdown("---")

st.markdown("""
Desenvolvido com:
- Python
- Spotify API
- YouTube API
- PostgreSQL
- Streamlit
""")