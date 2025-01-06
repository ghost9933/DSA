class DisjointUnionSets:
    def __init__(self, n):
        self.rank = [0] * n
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
          
            # Path compression
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unionSets(self, x, y):
        xRoot = self.find(x)
        yRoot = self.find(y)

        if xRoot == yRoot:
            return

        # Union by Rank   
        if self.rank[xRoot] < self.rank[yRoot]:
            self.parent[xRoot] = yRoot
        elif self.rank[yRoot] < self.rank[xRoot]:
            self.parent[yRoot] = xRoot
        else:
            self.parent[yRoot] = xRoot
            self.rank[xRoot] += 1

class Solution:
  


    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        uf=DisjointUnionSets(n)
        provinces=dict()
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j]==1:
                    uf.unionSets(i,j)
        p=set()
        for x in range(n):
            xp=uf.find(x)
            if xp not in p:
                p.add(xp)
        return len(p)

                    
                    