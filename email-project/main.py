import requests
import streamlit as st

topic = "Ai Hackathons"
st.set_page_config(layout="centered")

api_key = "aa15640c4b6149b4a67fc925aee56b21"
url = "https://newsapi.org/v2/everything?" \
       f"q={topic}&" \
       "from=2026-08-08&sortBy=publishedAt&apiKey=aa15640c4b6149b4a67fc925aee56b21&language=en"

request = requests.get(url)
content = request.json()

st.write("<h3>News app</h3>", unsafe_allow_html=True)

st.markdown("""
    <style>
    .article-title {
        display: -webkit-box;
        -webkit-line-clamp: 1;       /* max lines before truncating */
        -webkit-box-orient: vertical;
        overflow: hidden;
        text-overflow: ellipsis;
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 4px;
    }
    .article-desc {
        display: -webkit-box;
        -webkit-line-clamp: 3;       /* max lines before truncating */
        -webkit-box-orient: vertical;
        overflow: hidden;
        font-size: 0.91rem;
        font-weight: 500;
        text-overflow: ellipsis;
        color: #444;
    }
    </style>
""", unsafe_allow_html=True)


for article in content["articles"][:20]:
    if article["title"] is not None:
        text_col, image_col = st.columns([3, 2])

        with text_col:
            st.markdown(f'<div class="article-title">{article["title"]}</div>', unsafe_allow_html=True)
            if article["description"] is not None:
                st.markdown(f'<div class="article-desc">{article["description"]}</div>', unsafe_allow_html=True)
            st.write(article["url"])

        with image_col:
            if article["urlToImage"] is not None:
                st.image(article["urlToImage"])

        st.divider()