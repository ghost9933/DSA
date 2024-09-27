class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        cSum=0
        curr=dict()
        ans=0
        for i in range(len(nums)):
            s=nums[i]
            if s not in curr:
                curr[s]=1
            else:
                curr[s]+=1
            e=0
            if i>=k:
                e=nums[i - k]
                curr[e]-=1
                if curr[e]==0:
                    del curr[e]
            
            # print(i,s,e)
            cSum+=s-e
            # print(i,cSum)
            # print(curr)
            if len(curr)==k:
                ans=max(ans,cSum)
        return ans 
