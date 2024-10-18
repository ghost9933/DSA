class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        def strToMap(ins):
            d={}
            for x in ins:
                if x in d:
                    d[x]+=1
                else:
                    d[x]=1
            return d
        
        def isOdd(s):
            if len(s)%2==0:
                return False
            else:
                return True

        strMap=strToMap(s)
        oddCount=0
        for x in strMap:
            if strMap[x]%2!=0:
                oddCount+=1
        print(strMap,isOdd(s),oddCount)
        if isOdd(s) and oddCount==1:
            return True
        elif not isOdd(s) and oddCount==0:
            return True
        else:
            return False
        