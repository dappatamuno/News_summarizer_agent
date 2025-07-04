import streamlit as st
from fetch import fetch_news
from summarize import summarize_article
from categories import categorize

st.set_page_config(page_title="News Summarizer", layout="wide")
st.title("📰 AI News Aggregator & Summarizer")

st.sidebar.title("Options")
refresh = st.sidebar.button("🔄 Refresh News")

if refresh:
    news_data = fetch_news()
    st.session_state.news = news_data

if "news" not in st.session_state:
    st.session_state.news = fetch_news()

search = st.text_input("Search Articles", "")

for article in st.session_state.news:
    if search.lower() in article['title'].lower():
        summary = summarize_article(article['content'])
        category = categorize(article['title'], article['content'])

        st.subheader(article['title'])
        st.markdown(f"**Source:** [{article['source']}]({article['url']})")
        st.markdown(f"**Category:** {category}")
        st.markdown(summary)
        st.markdown("---")