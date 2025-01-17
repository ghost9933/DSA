class Trie:

    def __init__(self):
        self.root=dict()
        
    def insert(self, word: str) -> None:
        if word[0] not in self.root:
            self.root[word[0]]=dict()
        curr=self.root[word[0]]
        for x in word[1:]:
            if x not in curr:
                curr[x]=dict()
            curr=curr[x]
        curr['end']='end'

    def search(self, word: str) -> bool:
        # print(self.root)
        curr=self.root
        for x in word:
            if x not in curr:
                return False
            curr=curr[x]
        if 'end' in curr:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        curr=self.root
        for x in prefix:
            if x not in curr:
                return False
            curr=curr[x]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)