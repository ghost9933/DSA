class Solution:
    def numDecodings(self, s: str) -> int:
        one=1
        two=1
        if s[0]=='0':
            return 0
        for i in range(1,len(s)):
            curr=0
            if s[i]!='0':
                curr=one
            if 10<=int(s[i-1:i+1])<=26:
                curr+=two
            two=one
            one=curr
        return one
