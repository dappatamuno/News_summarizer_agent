import feedparser

RSS_FEEDS = [
    "http://feeds.bbci.co.uk/news/rss.xml",
    "https://rss.cnn.com/rss/edition.rss",
    "https://feeds.npr.org/1001/rss.xml"
]

def fetch_news():
    news_list = []
    for url in RSS_FEEDS:
        feed = feedparser.parse(url)
        for entry in feed.entries[:5]:
            news_list.append({
                'title': entry.title,
                'content': entry.summary,
                'url': entry.link,
                'source': feed.feed.title
            })
    return news_list