class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix_sum = [nums[0]]
        ans = []
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])
        
        for target in queries:
            l = 0
            r = len(nums) - 1
            pos = -2 # -2 for not found case
            #left bin search             
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    pos = mid
                    r = mid - 1     

            if pos == -2:
                pos = min(l, r)
            # pos == -1 leftmost case
            if pos == -1:
                ans.append(prefix_sum[-1] - (len(nums))*target)
            else:
                ans.append((pos+1)*target - prefix_sum[pos] + prefix_sum[-1] - prefix_sum[pos] - (len(nums) -1 - pos)*target)
            
        return ans