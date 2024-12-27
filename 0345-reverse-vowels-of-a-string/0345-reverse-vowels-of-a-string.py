class Solution:
    def reverseVowels(self, s: str) -> str:
        index=[]
        vowels=[]
        vowelSet={'a', 'e', 'i', 'o','u','A','E','I','O','U'}
        s=list(s)
        for i,char in enumerate(s):
            if char in vowelSet:
                index.append(i)
                vowels.append(char)
        index=index[::-1]
        while index:
            i=index.pop()
            c=vowels.pop()
            s[i]=c
        return ''.join(s)
            
            
            