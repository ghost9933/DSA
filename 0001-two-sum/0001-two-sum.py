class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen=dict()
        for i in range(len(nums)):
            lookup=target-nums[i]
            if lookup in seen :
                return [i,seen[lookup]]
            else:
                seen[nums[i]]=i
        return None

        
        