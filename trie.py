class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.pages_freq = {}   # key: page_name, value: frequency

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, page_name):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        node.pages_freq[page_name] = node.pages_freq.get(page_name, 0) + 1

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return {}
            node = node.children[char]
        return node.pages_freq if node.is_end else {}

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return {}
            node = node.children[char]
        return self._collect_pages(node)

    def _collect_pages(self, node):
        result = {}
        if node.is_end:
            for page, freq in node.page_freq.items():
                result[page] = result.get(page, 0) + freq
        for child in node.children.values():
            child_result = self._collect_pages(child)
            for page, freq in child_result.items():
                result[page] = result.get(page, 0) + freq
            return result