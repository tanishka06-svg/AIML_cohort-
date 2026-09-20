# RAG Fundamentals: Chunking and Retrieval

## 1. Text Corpus

A small text corpus is created manually with six short sections. Each
section talks about a different topic related to AI and RAG.

The topics include:

-   Artificial Intelligence
-   Machine Learning
-   Natural Language Processing
-   Large Language Models
-   Retrieval Augmented Generation
-   Embeddings

This keeps the example simple and makes it easier to understand what
each retrieval method is doing.

## 2. Fixed-Size Chunking

The corpus is divided into smaller pieces using fixed-size chunking.

The notebook uses:

-   Chunk size: 300 characters
-   Overlap: 50 characters

The overlap means that a small part of one chunk is repeated in the next
chunk. This helps retain some context when information falls near a
chunk boundary.

The chunks are cleaned using `strip()` before they are stored.

## 3. Dense Retrieval

For dense retrieval, the notebook uses the `all-MiniLM-L6-v2` model from
Sentence Transformers.

Each chunk is converted into an embedding vector. When a user enters a
query, the query is also converted into a vector. Cosine similarity is
then used to compare the query embedding with the chunk embeddings.

The top 3 most similar chunks are returned.

### Sample Queries

``` text
How does RAG retrieve information?
```

and

``` text
What are numerical representations of text?
```

The retrieved chunks are printed along with their similarity scores.

## 4. Sparse Retrieval with BM25

The same chunks are also searched using BM25.

Unlike dense retrieval, BM25 mainly depends on the words present in the
query and the documents. The chunks are tokenized and passed to
`BM25Okapi`, which calculates a relevance score for each chunk.

The same two queries are used so that the results from dense retrieval
and BM25 can be compared.

## 5. Dense Retrieval vs BM25

The two approaches work in slightly different ways.

**Dense retrieval** focuses more on the meaning of the query and the
stored text. It can still find related content when the wording is not
exactly the same.

**BM25** mainly looks at word-level matching. It can work especially
well when important keywords from the query also appear in the relevant
document.

Using both approaches gives a useful idea of the difference between
semantic search and keyword-based search.

## 6. Technologies Used

-   Python
-   Sentence Transformers
-   Scikit-learn
-   NumPy
-   rank_bm25
-   Google Colab / Jupyter Notebook

### Summary

This notebook is a small hands-on implementation of basic RAG retrieval
techniques. It takes a simple text corpus, breaks it into overlapping
chunks, and then compares dense retrieval using embeddings with
BM25-based sparse retrieval.