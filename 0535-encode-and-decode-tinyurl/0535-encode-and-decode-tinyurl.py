class Codec:
    def __init__(self):
        self.active=dict()
        self.last=0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        # while self.last in self.active:
        #     self.last+=1
        # self.last+=1
        # self.active[self.last]=longUrl
        # return "http://tinyurl.com/"+str(self.last)
        asciis = []
        for i in longUrl:
            value = str(ord(i))
            # we need all ascii values with length three so apdding prefix with 0
            value = '0'*(3-len(value)) + value 
            asciis.append(value)
        
        asciis = ''.join(asciis)
        if len(asciis) > 4300:
            sys.set_int_max_str_digits(len(asciis) + 1) 
        asciis = int(asciis)
        ans = hex(asciis)
        # print(longUrl)
        # print(ans)
        return ans

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        # id=shortUrl[19:]
        # print('id',id)
        # return self.active[int(id)]
        # print(shortUrl)
        n = int(shortUrl, 16)
        # print(n)
        ans = []
        while n >0:
            lastThreeDigits = n % 1000
            n = n // 1000
            ans.append(chr(lastThreeDigits))

        ans = ans[::-1]
        return ''.join(ans)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))