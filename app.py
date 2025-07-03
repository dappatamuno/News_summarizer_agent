import streamlit as st
from aggregator import fetch_articles
from summarizer import summarize_texts
from keywords import extract_keywords
from vector_search import build_vector_index, query_index

st.title("📰 News Aggregator & Summarizer Agent")

query = st.text_input("🔎 Enter a keyword or topic (e.g. climate, economy):", "")

if query:
    st.info("Fetching news articles...")
    articles = fetch_articles(query)
    if not articles:
        st.warning("No articles found.")
    else:
        st.success(f"Found {len(articles)} articles. Summarizing...")
        summaries = summarize_texts([a['text'] for a in articles])
        index = build_vector_index([s['summary'] for s in summaries])

        user_question = st.text_input("💬 Ask something about the news:")
        if user_question:
            result = query_index(user_question, index, [s['summary'] for s in summaries])
            st.markdown("### 🔍 Top Relevant Summary:")
            st.write(result)

        st.markdown("---")
        st.markdown("## 📰 Articles & Summaries")
        for i, (article, summary) in enumerate(zip(articles, summaries)):
            st.subheader(f"{i+1}. {article['title']}")
            st.markdown(f"**Source**: {article['url']}")
            st.markdown(f"**Keywords**: {', '.join(extract_keywords(article['text']))}")
            st.markdown("**Summary**:")
            st.write(summary['summary'])
            st.markdown("---")