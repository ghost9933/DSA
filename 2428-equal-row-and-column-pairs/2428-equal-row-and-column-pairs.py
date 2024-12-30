class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows=[]
        cols=[[] for i in range(len(grid[0]))]
        print(cols)
        for i in range(len(grid)):
            rows.append(tuple(grid[i]))
            for j in range(len(grid[0])):
                cols[j].append(grid[i][j])
        for i in range(len(cols)):
            cols[i]=tuple(cols[i])
        print(rows)
        print(cols)
        ans=0
        for x in cols:
            for j in rows:
                if x==j:
                    ans+=1
        return ans
