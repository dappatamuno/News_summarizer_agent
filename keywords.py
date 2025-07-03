import yake

def extract_keywords(text):
    kw_extractor = yake.KeywordExtractor(top=5, stopwords=None)
    keywords = kw_extractor.extract_keywords(text)
    return [kw for kw, _ in keywords]