TOPICS = {
    "Politics": ["election", "government", "president", "senate"],
    "Technology": ["AI", "tech", "software", "startup"],
    "Health": ["health", "virus", "covid", "hospital"],
    "Business": ["market", "stock", "business", "trade"],
    "Sports": ["football", "soccer", "tennis", "olympics"]
}

def categorize(title, text):
    combined = (title + " " + text).lower()
    for category, keywords in TOPICS.items():
        if any(keyword.lower() in combined for keyword in keywords):
            return category
    return "Other"