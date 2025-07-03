from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def build_vector_index(texts):
    embeddings = model.encode(texts)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))
    return {"index": index, "texts": texts, "embeddings": embeddings}

def query_index(query, index_data, texts):
    query_vec = model.encode([query])
    D, I = index_data["index"].search(np.array(query_vec), k=1)
    return texts[I[0][0]]