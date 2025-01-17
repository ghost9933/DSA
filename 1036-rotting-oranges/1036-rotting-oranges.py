class Solution:

    def orangesRotting(self,grid):
        if not grid:
            return -1
        
        rows = len(grid)
        cols = len(grid[0])
        
        fresh_oranges = set()
        rotten_oranges = deque()
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    rotten_oranges.append((i, j))
                elif grid[i][j] == 1:
                    fresh_oranges.add((i, j))
        
        if not rotten_oranges and not fresh_oranges:
            return 0
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        minutes = 0
        while rotten_oranges:
            if not fresh_oranges:
                return minutes
            
            for _ in range(len(rotten_oranges)):
                x, y = rotten_oranges.popleft()
                for dx, dy in directions:
                    tx, ty = x + dx, y + dy
                    if 0 <= tx < rows and 0 <= ty < cols and (tx, ty) in fresh_oranges:
                        fresh_oranges.remove((tx, ty))
                        rotten_oranges.append((tx, ty))
            
            minutes += 1
        
        return -1 if fresh_oranges else minutes - 1
