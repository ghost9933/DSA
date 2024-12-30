class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a=set(nums1)
        b=set(nums2)
        ans=[[],[]]
        for x in a:
            if x not in b:
                ans[0].append(x)
        for x in b:
            if x not in a:
                ans[1].append(x)
        return ans 