class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        xmap={}
        ymap={}
        for x in s:
            if x in xmap:
                xmap[x]+=1
            else:
                xmap[x]=1
        
        for y in t:
            if y in ymap:
                ymap[y]+=1
            else:
                ymap[y]=1
        # print(xmap,"\n",ymap)
        if xmap==ymap:
            return True
        else :
            return False
        
