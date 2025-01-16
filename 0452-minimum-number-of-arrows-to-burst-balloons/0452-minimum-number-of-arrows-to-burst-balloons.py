class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points=sorted(points,key=lambda x:x[1])
        k=-math.inf
        ac=0
        for x1,x2 in points:
            if x1>k:
                k=x2
                ac+=1
        return ac
        
