from transformers import pipeline

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_texts(texts):
    summaries = []
    for text in texts:
        short_text = text[:1024]  # truncation for smaller models
        summary = summarizer(short_text, max_length=130, min_length=30, do_sample=False)[0]["summary_text"]
        summaries.append({"summary": summary})
    return summaries