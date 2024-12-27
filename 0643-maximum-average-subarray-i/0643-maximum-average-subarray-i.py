class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
    
        i=0
        oNum=0
        cSum=0
        ans=-math.inf
        # if k==1:
        #     return max(nums)
        # if k==len(nums):
        #     return sum(nums)/k
        while i <k:
            cSum+=nums[i]
            i+=1
        ans=cSum/k
        while i in range(k,len(nums)):
            if i<k:
                cSum+=nums[i]
                oNum=0
            else:
                cSum-=nums[oNum]
                cSum+=nums[i]
                oNum+=1
            ans=max(ans,cSum/k)
            i+=1
        return ans 

                