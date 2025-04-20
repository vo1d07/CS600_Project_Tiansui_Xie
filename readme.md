# Webpage Search Engine Using Trie

This project implements a simple search engine that builds a trie-based index from a small collection of HTML pages downloaded from Wikipedia. Users can query a keyword, and the program will return a ranked list of pages where the keyword appears, based on term frequency (TF).

---

## Trie.py

This module defines a `Trie` data structure for indexing and searching words from multiple HTML pages. Each node stores frequency information for each word per page, enabling ranking by term frequency (TF).

---

### Classes

#### `TrieNode`
A node in the trie.

- `children`: Dictionary mapping characters to child nodes.
- `is_end`: Boolean indicating if the current node marks the end of a word.
- `pages_freq`: Dictionary `{page_name: frequency}` recording the term frequency per page.

#### `Trie`
The main trie structure.

- `insert(word, page_name)`:  
  Inserts a word into the trie and updates its frequency for the given page.

- `search(word) → dict`:  
  Returns a dictionary `{page_name: frequency}` for an exact word match.

- `starts_with(prefix) → dict`:  
  Returns aggregated frequencies of all words that begin with the given prefix.

- `_collect_pages(node)`:  
  Helper method to recursively gather frequency info from a subtree.

---

### Example

```python
trie = Trie()
trie.insert("search", "page1.html")
trie.insert("search", "page1.html")
trie.insert("searching", "page2.html")

print(trie.search("search"))       # {'page1.html': 2}
print(trie.starts_with("sear"))    # {'page1.html': 2, 'page2.html': 1}
```

---

## utils.py

This module provides utility functions for preprocessing HTML documents and loading stopwords. It is used in the simplified search engine project to extract clean tokens from web pages.

---

### Functions

### `extract_text_from_html(file_path)`
Extracts and tokenizes visible text from an HTML file.

- **Parameters**:
  - `file_path` (str): Path to the HTML file.
- **Returns**:
  - `List[str]`: A list of lowercased, punctuation-free word tokens.

- **Processing steps**:
  - Removes `<script>` and `<style>` tags.
  - Converts text to lowercase.
  - Removes punctuation using regex (`[^\w\s]`).
  - Splits the text into tokens by whitespace.

---

#### `load_stopwords(file_path)`
Loads a list of stopwords from a plain text file.

- **Parameters**:
  - `file_path` (str): Path to the stopword list file.
- **Returns**:
  - `Set[str]`: A set of stopwords.

- **Expected format**:
  - One stopword per line, UTF-8 encoded file.

---

### Example

```python
tokens = extract_text_from_html("webpages/page1.html")
stopwords = load_stopwords()
clean_tokens = [t for t in tokens if t not in stopwords]
```

---

## search_engine.py

This script is the main entry point of the simplified search engine. It processes a collection of HTML files, builds a trie-based index of word occurrences, and allows users to perform keyword-based searches with term frequency–based ranking.

---

### Processing Steps

1. **Stopword Loading**  
   Loads a set of common English stopwords from `stopwords.txt`, which are excluded from indexing to reduce noise.

2. **Webpage Parsing**  
   Iterates through all `.html` files in the `webpages/` directory and uses `extract_text_from_html()` to:
   - Remove `<script>` and `<style>` tags.
   - Lowercase and clean punctuation.
   - Tokenize into individual words.

3. **Trie Index Construction**  
   Each valid token (i.e., not a stopword) is inserted into the `Trie` data structure.
   - Each trie node stores the frequency of the word in each HTML page.

---

### Keyword Search

The user is prompted to input a single keyword. The system:
- Looks up the word in the trie.
- Returns a list of pages where the word appears.
- **Sorts results by term frequency** (TF), from highest to lowest.