class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        setVowels={'a','e','i','o','u'}
        c=0
        i=0
        while i<k:
            if s[i] in setVowels:
                c+=1
            i+=1
        out=0
        ans=c
        # print('init max i',ans,i)
        while i<len(s):
            # print('in loop max i',ans,i,'\t',s[out+1:i+1])
            if s[out] in setVowels:
                c-=1
            if s[i] in setVowels:
                c+=1
            out+=1
            i+=1
            ans=max(ans,c)
        return ans


            