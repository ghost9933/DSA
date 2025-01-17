class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=[]

        r=[]
        for  i in nums:
            l.append(i)
            r.append(i)
        left=-1
        right=1
        i=1
        while i<len(nums):
            if i>0:
                l[i]=l[i-1]*l[i]
            i+=1
        i=len(nums)-1
        print(l)
        while i>=0:
            if i!=len(nums)-1:
                r[i]=r[i+1]*r[i]
            i-=1
        print(r)
        ans=[]
        for i in range(len(nums)):
            if i ==0:
                ans.append(r[1])
            elif i==len(nums)-1:
                ans.append(l[i-1])
            else:
                ans.append(l[i-1]*r[i+1])
        return ans 

