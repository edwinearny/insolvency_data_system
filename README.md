# UK Insolvency Information Retrieval System


## How It Works

The system processes UK insolvency law files, converts them into vector embeddings and stores them in vector database. The system improves user queries through spell checking and stop-word elimination before it obtains the most relevant document chunks through semantic search and uses a cross-encoder model to enhance result accuracy.
## Key Components

- **Data Layer** — Loads PDF documents, splits them into chunks, creates vector embeddings and stores them in ChromaDB.
- **Query Intelligence** — Cleans punctuation, corrects spelling mistakes and removes stop words to improve search accuracy.
- **Ranking Engine** — Uses cross-encoder to re-rank search results for more accurate results.
- **User Interface** — A Streamlit web app for real-time and result display.

Sample outputs:
![Screenshot](sample_output.png)

## Tech Stack

- Python
- ChromaDB (Vector Database)
- Sentence Transformers (Embeddings & Re-ranking)
- Streamlit (UI)
- NLTK & PySpellChecker (Query Processing)

## Setup
```bash
pip install -r requirements.txt
python build.py
streamlit run app.py
```
