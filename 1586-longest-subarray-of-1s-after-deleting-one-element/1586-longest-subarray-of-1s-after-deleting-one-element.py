class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if len(nums)<1:
            return 0
        zCount=0
        s=[]
        op=-1
        i=0
        ans=0
        while i<len(nums):
            # print(i)
            if nums[i]==0:
                s.append(i)
                zCount+=1
            # print(i,zCount,'ans',ans,s)
            if zCount>1:
                op=s.pop(0)
                zCount-=1
            ans=max(ans,i-op-1)
            # print('stack',s,'\t i',i,'out',op,'\t',ans)
            i+=1

        return ans
