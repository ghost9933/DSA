class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n=0
        m=0
        ans=''
        while n<=len(word1)-1 and m<=len(word2)-1:
            ans=ans+word1[n]+word2[m]
            n+=1
            m+=1
        if n<=len(word1)-1:
            for i in range(n,len(word1)):
                ans=ans+word1[i]
        if m<=len(word2)-1:
            for i in range(n,len(word2)):
                ans=ans+word2[i]
        return ans

