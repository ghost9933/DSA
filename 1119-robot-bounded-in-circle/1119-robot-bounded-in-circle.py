class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        d=None
        current=[[0,0],0]
        visited=set()
        for inst in instructions:
            if inst=='G':
                if current[1]==90:
                    current[0][0]+=1
                elif current[1]==0:
                    current[0][1]+=1
                elif current[1]==180:
                    current[0][1]-=1
                elif current[1]==270:
                    current[0][0]-=1
            if inst=='L':
                if current[1]==0:
                    current[1]=270
                else:
                    current[1]-=90
            if inst=='R':
                if current[1]==270:
                    current[1]=0
                else:
                    current[1]+=90
        if current[0]==[0,0] or  current[1]!=0:
            return True 
        return False 