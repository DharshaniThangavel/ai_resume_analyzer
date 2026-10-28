from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load lightweight sentence transformer model once during server startup
model = SentenceTransformer('all-MiniLM-L6-v2')

def calculate_semantic_similarity(resume_text, jd_text):
    """
    Computes cosine similarity score between resume and JD embeddings.
    Returns a score between 0 and 100.
    """
    if not resume_text or not jd_text:
        return 0.0

    # Encode both texts into embedding vectors
    embeddings = model.encode([resume_text, jd_text])
    
    # Calculate cosine similarity
    similarity = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    
    # Convert from [-1, 1] or [0, 1] scale to a clean 0-100 percentage
    score = float(similarity) * 100
    return round(max(0.0, min(score, 100.0)), 2)