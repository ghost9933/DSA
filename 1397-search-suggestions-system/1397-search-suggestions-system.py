from typing import List

class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = [None] * 26  # 26 slots for 'a' to 'z'

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.result_buffer = []

    def dfs_with_prefix(self, node: TrieNode, word: str):
        # Stop when we have found 3 words
        if len(self.result_buffer) == 3:
            return
        if node.is_word:
            self.result_buffer.append(word)
        
        # Explore all children of the current node
        for i in range(26):  # Iterate over 'a' to 'z'
            child = node.children[i]
            if child is not None:
                self.dfs_with_prefix(child, word + chr(i + ord('a')))

    def insert(self, word: str):
        # Insert a word into the trie
        curr = self.root
        for char in word:
            index = ord(char) - ord('a')
            if curr.children[index] is None:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.is_word = True

    def get_words_starting_with(self, prefix: str) -> List[str]:
        # Find words that start with the given prefix
        curr = self.root
        self.result_buffer = []
        for char in prefix:
            index = ord(char) - ord('a')
            if curr.children[index] is None:
                return self.result_buffer
            curr = curr.children[index]
        self.dfs_with_prefix(curr, prefix)
        return self.result_buffer

class Solution:
    def suggestedProducts(self, products: List[str], search_word: str) -> List[List[str]]:
        trie = Trie()
        result = []

        # Insert all products into the trie
        for product in products:
            trie.insert(product)
        
        prefix = ""
        for char in search_word:
            prefix += char
            result.append(trie.get_words_starting_with(prefix))
        
        return result
