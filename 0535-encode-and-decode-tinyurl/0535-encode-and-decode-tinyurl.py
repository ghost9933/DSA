class Codec:
    def __init__(self):
        self.active=dict()
        self.last=0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        while self.last in self.active:
            self.last+=1
        self.last+=1
        self.active[self.last]=longUrl
        return "http://tinyurl.com/"+str(self.last)
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        id=shortUrl[19:]
        # print('id',id)
        return self.active[int(id)]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))