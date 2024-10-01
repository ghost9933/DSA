class Solution:
    # def combinationSum4(self, nums: List[int], target: int) -> int:

    #     #  top down approach
    #     map={}
    #     res=0
    #     end=len(nums)
    #     @lru_cache(maxsize = None)
    #     def backtrack(r):
    #         # print(map)
    #         if r==0:
    #             return 1
    #         if r in map:
    #             return map[r]
    #         c=0
    #         for x in nums:
    #             if r-x>=0:
    #                 c+=backtrack(r-x)
    #         map[r]=c
    #         return c
    #     return backtrack(target)
# bottom up approach
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # minor optimization
        # nums.sort()
        dp = [0 for i in range(target+1)]
        dp[0] = 1

        for comb_sum in range(target+1):

            for num in nums:
                if comb_sum - num >= 0:
                    dp[comb_sum] += dp[comb_sum-num]
                # minor optimization, early stopping.
                # else:
                #    break
        return dp[target]
