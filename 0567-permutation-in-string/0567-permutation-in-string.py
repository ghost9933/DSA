class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def strToDict(s:str):
            Smap={}
            for x in s:
                if x in Smap:
                    Smap[x]+=1
                else:
                    Smap[x]=1
            return Smap
        window=len(s1)
        sub=strToDict(s1)
        print('sub',sub)
        curr=''
        currMap={}
        for i in range (len(s2)):
            enter=s2[i]
            exiting=None
            if len(curr)>=window:
                exiting=curr[0]
                curr=curr[1:]

            curr+=s2[i]
            if s2[i] in currMap:
                currMap[s2[i]]+=1
            else:
                currMap[s2[i]]=1
            if exiting:
                currMap[exiting]-=1
                if currMap[exiting]==0:
                    del currMap[exiting]
            if currMap==sub:
                return True
        return False
            