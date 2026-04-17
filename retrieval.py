import os

KNOWLEDGE_FILE = "knowledge.txt"

def load_knowledge():
    if not os.path.exists(KNOWLEDGE_FILE):
        return []
    with open(KNOWLEDGE_FILE, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines() if line.strip()]

def retrieve_context(query, top_k=3):
    knowledge_lines = load_knowledge()
    query_words = set(query.lower().split())

    scored = []
    for line in knowledge_lines:
        line_words = set(line.lower().split())
        score = len(query_words.intersection(line_words))
        scored.append((score, line))

    scored.sort(reverse=True, key=lambda x: x[0])
    best = [line for score, line in scored[:top_k] if score > 0]

    return "\n".join(best)
