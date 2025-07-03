import newspaper

def fetch_articles(query):
    # Using preset sources for simplicity
    sources = [
        "https://www.reuters.com",
        "https://www.bbc.com/news",
        "https://www.cnn.com"
    ]
    articles = []
    for url in sources:
        paper = newspaper.build(url, memoize_articles=False)
        for article in paper.articles[:5]:
            try:
                article.download()
                article.parse()
                if query.lower() in article.text.lower():
                    articles.append({
                        "title": article.title,
                        "text": article.text,
                        "url": article.url
                    })
            except:
                continue
    return articles