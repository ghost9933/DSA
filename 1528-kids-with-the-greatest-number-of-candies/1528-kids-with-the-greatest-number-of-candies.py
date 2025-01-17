class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        l=max(candies)
        ans=[]
        for x in candies:
            if x +extraCandies>=l:
                ans.append(True)
            else:
                ans.append(False)
            
        return ans 