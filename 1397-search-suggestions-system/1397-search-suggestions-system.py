class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []  # Keep the words sorted during insertion

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            if len(node.words) < 3:  # Only store the top 3 words
                node.words.append(word)

    def get_words_starting_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return node.words

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for product in sorted(products):  # Sort products before inserting
            trie.insert(product)
        
        result = []
        prefix = ""
        for char in searchWord:
            prefix += char
            result.append(trie.get_words_starting_with(prefix))
        return result
