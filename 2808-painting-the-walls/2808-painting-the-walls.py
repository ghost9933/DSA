class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n=len(cost)
        # def dp(i,rem):
        #     if rem<=0:
        #         return 0
        #     if i==n:
        #         return math.inf
        #     paint=cost[i]+dp(i+1,rem-1-time[i])
        #     nopaint=dp(i+1,rem)
        #     return min(paint,nopaint)
        # return dp(0,n)
        n = len(cost)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            dp[n][i] = inf

        for i in range(n - 1, -1, -1):
            for remain in range(1, n + 1):
                paint = cost[i] + dp[i + 1][max(0, remain - 1 - time[i])]
                dont_paint = dp[i + 1][remain]
                dp[i][remain] = min(paint, dont_paint)
        
        return dp[0][n]

        dp=[[0]*(n+1)]*(n+1)
        for i in range(1,n+1):
            dp[n][i]=math.inf
        for i in range(n-1,-1,-1):
            for j in range(1,n+1):
                paint=cost[i]+dp[i+1][max(0,j-1-time[i])]
                nopaint=dp[i+1][j]
                dp[i][j]=min(paint,nopaint)
        return dp[0][n]

        
