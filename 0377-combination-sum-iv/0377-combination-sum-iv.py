class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        #  brute force 2^n
        map={}
        res=0
        end=len(nums)
        lru_cache(maxsize = None)
        def backtrack(r):
            # print(map)
            if r==0:
                return 1
            if r in map:
                return map[r]
            c=0
            for x in nums:
                if r-x>=0:
                    c+=backtrack(r-x)
            map[r]=c
            return c
        return backtrack(target)
        return res
            
            