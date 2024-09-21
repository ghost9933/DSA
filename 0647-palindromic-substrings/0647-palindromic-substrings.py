class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0

        if n == 0:
            return 0

        dp = [[False] * n for _ in range(n)]

        # Base case: single letter substrings
        for i in range(n):
            dp[i][i] = True
            ans += 1
            

        # Base case: double letter substrings
        for i in range(n - 1):
            dp[i][i + 1] = (s[i] == s[i + 1])
            if dp[i][i + 1]:
                ans += 1
       
        # All other cases: substrings of length 3 to n
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                
                j = i + length - 1
                # print(i,j)
                
                dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])
                if dp[i][j]:
                    ans += 1
                

        return ans
