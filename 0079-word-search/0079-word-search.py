class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        xLimit=len(board)
        yLimit=len(board[0])
        deltas=[(0,1),(-1,0),(1,0),(0,-1)]
        def dfsSearch(rem,curr,visited):
            nv=[]
            if rem[0] ==board[curr[0]][curr[1]]:
                nv=set(visited)
                nv.add(curr)
            else:
                return
            rem=rem[1:]
            if len(rem)==0:
                return True
            ans=False
            for x,y in deltas:
                
                dx=x+curr[0]
                dy=y+curr[1]
                if (dx,dy) not in nv and 0<=dx<xLimit and 0<=dy<yLimit:
                    ans=ans or dfsSearch(rem,(dx,dy),nv)
            return ans 

        for i in range(xLimit):
            for j in range(yLimit):

                if board[i][j] ==word[0]:
                    ispresent=dfsSearch(word,(i,j),set())
                    if ispresent:
                        return True
        return False