def get_chunks():
    with open("data/childhood_laws_tamilnadu.txt", "r", encoding="utf-8") as f:
        text = f.read()
    return text.split("\n\n")  # paragraph chunking

def vectorize_chunks(chunks):
    from sklearn.feature_extraction.text import TfidfVectorizer
    vec = TfidfVectorizer()
    return vec.fit_transform(chunks), vec

def get_relevant_chunk(query, chunks, vec_data):
    vectors, vec = vec_data
    query_vec = vec.transform([query])
    from sklearn.metrics.pairwise import cosine_similarity
    sim = cosine_similarity(query_vec, vectors)
    idx = sim.argmax()
    return chunks[idx]
