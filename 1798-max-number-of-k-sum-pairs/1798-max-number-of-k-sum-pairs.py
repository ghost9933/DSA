class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        seen=dict()
        ans=0
        for x in nums:
            # print(seen)
            lk=k-x
            if lk in seen  and seen[lk]>=1:
                print(lk,x)
                seen[lk]-=1
                ans+=1
            else:
                if x not in seen:
                    seen[x]=0
                seen[x]+=1
        return ans    
