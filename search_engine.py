import os
from trie import Trie
from utils import extract_text_from_html, load_stopwords

# Initialize
trie = Trie()
stopwords = load_stopwords()

# Setup indexes pages by pages
for file in os.listdir("webpages"):
    if file.endswith(".html"):
        tokens = extract_text_from_html(os.path.join("webpages", file))
        for token in tokens:
            if token not in stopwords:
                trie.insert(token, file)
 
# Inquiry procedure
while True:
    query = input("Enter the keyword (or enter 'quit' to quit): ").lower()
    if query == 'quit':
        break

    result = trie.search(query)
    if result:
        print(f"Keyword \"{query}\" appears in these pages (sort by frequency):")
        for page, freq in sorted(result.items(), key=lambda x: x[1], reverse=True):
            print(f" - {page} (frequency: {freq})")
    else:
        print("No matched pages found.")