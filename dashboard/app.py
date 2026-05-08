import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="Spotify & YouTube Analytics",
    layout="wide",
    page_icon="🎵"
)


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


st.title("🎵 Spotify & YouTube Analytics Dashboard")

st.markdown("""
Análise de tendências musicais e audiovisuais
""")


avg_popularity = spotify['popularity'].mean()

total_views = youtube['views'].sum()

avg_engagement = youtube['engagement'].mean()

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
    yaxis_title="Popularidade"
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
    yaxis_title="Visualizações"
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

st.plotly_chart(
    fig_engagement,
    use_container_width=True
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