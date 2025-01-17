class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
    
        r=0
        sc=math.floor(h/len(piles))
        r=h-sc*len(piles)
        print(sc,r)
        e=math.ceil(max(piles)/sc)
        s=1
        while e>s:
            m=(e+s)//2
            spent=0
            for x in piles:
                spent+=math.ceil(x/m)
            if spent<=h:
                e=m
            else:
                s=m+1
        return e
                

            
        