class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        if area==0:
            return [0,0]
        opWidth=1
        mindiff=math.inf
        for l in range(area,1,-1):
            if area%l!=0:
                continue
            w=area/l
            print(l,w)
            if l<w:
                break
            if l-w<mindiff:
                mindiff=l-w
                opWidth=w
        return [int(area/opWidth),int(opWidth)]