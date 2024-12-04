class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        #  for any fgiven elemnt i have two options to include it or to exclude it
        dp = [defaultdict(int) for i in range(k + 1)]
        res = [0] * (k + 1)
        for x in nums:
            for i in range(k,-1,-1):
                dp[i][x] = max(dp[i][x] + 1, res[i - 1] + 1 if i else 0)
                res[i] = max(res[i], dp[i][x])
        return res[k]

            
