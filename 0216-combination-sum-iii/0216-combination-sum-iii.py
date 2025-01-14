class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans=[]
        def find(used,rem):
            if rem==0 and len(used)==k:
                x=sorted(used)
                if x not in ans:
                    ans.append(list(x))
                return
            if len(used)>k:
                return 
            for i in  range(1,10):
                if i not in used:
                    used.append(i)
                    find(used,rem-i)
                    used.pop()

        find([],n)
        return ans 
            