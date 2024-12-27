import math

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        minSoFar = nums[0]
        for i in range(1, len(nums) - 1):
            current = nums[i]
            if minSoFar >= current:
                nums[i] = -math.inf
            
            minSoFar = min(minSoFar, current)

        maxSoFar = nums[-1]
        for i in range(len(nums) - 2, 0, -1):
            if nums[i] == -math.inf:
                continue

            if nums[i] < maxSoFar:
                return True

            maxSoFar = max(maxSoFar, nums[i])

        return False