from src.query import enhance_query, correct_spelling, remove_stop_words

queries = [
    "whta is insolvncy?",
    "How does liquidation work in the UK?",
    "compny cant pay debts",
    "what is a moratorium?",
]

for q in queries:
    print(f"Original:  {q}")
    print(f"Enhanced:  {enhance_query(q)}")
    print()
