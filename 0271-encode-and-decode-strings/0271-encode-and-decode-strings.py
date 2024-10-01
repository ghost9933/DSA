class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        out=''
        delimeter='$$ $$'
        for x in strs:
            out=out+x+delimeter
        return out

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings
        """
        print(s)
        t=''
        ans=[]
        n=len(s)
        i=0
        while i<n:
            print(s[i])
            if s[i]+s[i+1]+s[i+2]+s[i+3]+s[i+4]=='$$ $$':
                ans.append(t)
                t=''
                i+=5
            else:
                t=t+s[i]
                i+=1
        return ans

        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))