# 🧠 News Aggregator & Summarizer Agent

This project builds an intelligent agent that scrapes news articles, summarizes their content using open-source language models, extracts keywords, and enables semantic search using FAISS. It uses only **free and open-source tools** and is ready to deploy on **Streamlit Cloud** or **Hugging Face Spaces**.

## 🚀 Features

- Scrape news from trusted sources (BBC, CNN, Reuters)
- Summarize news using a fine-tuned BART model (`distilbart-cnn-12-6`)
- Extract top keywords from articles using YAKE
- Search summaries with semantic vector search (FAISS + Sentence Transformers)
- Interactive web UI with Streamlit

## 🛠 Tech Stack

- `newspaper3k` – News scraping
- `transformers` – Text summarization
- `yake` – Keyword extraction
- `sentence-transformers` + `faiss-cpu` – Semantic vector search
- `streamlit` – Frontend interface

## 📂 Folder Structure

```
news_summarizer_agent/
├── app.py               # Streamlit app
├── aggregator.py        # News scraping
├── summarizer.py        # Text summarization
├── keywords.py          # Keyword extraction
├── vector_search.py     # Vector indexing & search
├── requirements.txt     # Python dependencies
└── README.md            # Project overview
```

## 📦 Installation

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 🌐 Deployment

You can deploy this project for free via:

- [Streamlit Cloud](https://streamlit.io/cloud)
- [Hugging Face Spaces](https://huggingface.co/spaces)

## 🤝 Contribution

Contributions and improvements are welcome! Please fork this repo and submit a PR.

## 📄 License

MIT License