# 📰 News Aggregator & Summarizer

This app collects trending news from multiple sources and summarizes each article using an open-source NLP model. It's fully open source, easy to deploy, and runs on free-tier infrastructure.

## 💡 Features
- Auto-fetches latest news from RSS feeds or web scraping
- Summarizes articles using `distilbart-cnn`
- Categorizes summaries by topic
- Easy-to-use Streamlit interface
- Deployable on Streamlit Cloud or Hugging Face Spaces

## 🚀 Deployment
- Streamlit Cloud: https://share.streamlit.io

## 🛠 Tech Stack
- Python
- Streamlit
- HuggingFace Transformers
- Feedparser / Newspaper3k

## 📦 Setup
```bash
pip install -r requirements.txt
streamlit run app.py
```