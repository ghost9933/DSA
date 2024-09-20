class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
    
        def backtrack(i, sum):
            if i == len(nums):
                return 1 if sum == target else 0
            
            # Check memoization
            if (i, sum) in memo:
                return memo[(i, sum)]
            
            # Calculate ways for current state
            add = backtrack(i + 1, sum + nums[i])
            subtract = backtrack(i + 1, sum - nums[i])
            
            # Store in memo and return the total
            memo[(i, sum)] = add + subtract
            return memo[(i, sum)]

        return backtrack(0, 0)
            
