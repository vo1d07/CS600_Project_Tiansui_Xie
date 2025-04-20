from bs4 import BeautifulSoup
import re

def extract_text_from_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, "html.parser")

    # Remove redundant tags
    for tag in soup(["script", "style"]):
        tag.decompose()
    
    text = soup.get_text(separator=" ", strip=True)
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text.split()

def load_stopwords(file_path="stopwords.txt"):
    with open(file_path, "r", encoding="utf-8") as f:
        return set(word.strip() for word in f)