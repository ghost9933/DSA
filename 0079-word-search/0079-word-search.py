class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        v={}
        # /in case there were n words/
        # trie={}
        # for w in word:
        #     root=trie
        #     for i in w:
        #         if i not in root:
        #             root[i]={}
        #         root=root[i]
        #     root['end']=word
        # print(trie)
        # for x in trie:
        #     print(x)

        xLimit=len(board)
        yLimit=len(board[0])
        deltas=[(0,1),(-1,0),(1,0),(0,-1)]
        def dfsSearch(rem,curr,visited):
            # print(curr,rem)
            nv=[]
            if rem[0] ==board[curr[0]][curr[1]]:
                nv=nv+visited+[(curr)]
            else:
                return
            rem=rem[1:]
            # print(curr,rem,visited)
            if len(rem)==0:
                # print('found at',visited,curr)
                return True
            ans=False
            for x,y in deltas:
                
                dx=x+curr[0]
                dy=y+curr[1]
                # print('check',(dx,dy))
                
                if (dx,dy) not in nv and 0<=dx<xLimit and 0<=dy<yLimit:
                    ans=ans or dfsSearch(rem,(dx,dy),nv[:])
            return ans 

        # print(xLimit,yLimit)
        for i in range(xLimit):
            # print(i,"_")
            for j in range(yLimit):
                # print("_",j)
                # print('enterning ',(i,j))
                if board[i][j] ==word[0]:
                    ispresent=dfsSearch(word,(i,j),[])
                    if ispresent:
                        return True
        return False