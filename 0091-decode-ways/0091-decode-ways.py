class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        @lru_cache
        def ways(i):
            
            if i==n:
                return 1
            if s[i]=='0':
                return 0
            if i==n-1:
                return 1
            
            ans=ways(i+1)
            if int(s[i:i+2])<=26:
                ans+=ways(i+2)
            return ans 
        return ways(0)