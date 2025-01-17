class Solution:
    
    def tribonacci(self, n: int) -> int:
        mapF=dict({0:0,1:1,2:1})
        def find(n):
            
            nonlocal mapF
            # print(n,mapF)
            if n in mapF:
                return mapF[n]
            else :
                x=find(n-3)+find(n-2)+find(n-1)
                # print(n,x)
                mapF[n]=x
                return mapF[n]
        # print(mapF)
        return find(n)
        