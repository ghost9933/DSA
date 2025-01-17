class Solution:
    def rob(self, nums: List[int]) -> int:
        dp=[0]*(len(nums)+1)
        print(dp)
        dp[1]=nums[0]
        for i in range(2,len(nums)+1):
            dp[i]=max(dp[i-2]+nums[i-1],dp[i-1])
        print(dp)
        return dp[-1]