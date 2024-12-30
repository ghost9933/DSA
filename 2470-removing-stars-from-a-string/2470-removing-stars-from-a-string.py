class Solution:
    def removeStars(self, s: str) -> str:
        ans=[]
        for x in s:
            if x=='*':
                ans.pop()
            else:
                ans.append(x)
        return ''.join(ans)