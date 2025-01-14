class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitMap={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        ans=[]
        def trav(d,c):
            nonlocal ans
            if len(d)<=0:
                if c!='':
                    ans.append(c)
                return
            chars=digitMap[d[0]]
            for x in chars:
                # print(x,d[1:],c+x)
                trav(d[1:],c+x)
        trav(digits,'')
        return ans    