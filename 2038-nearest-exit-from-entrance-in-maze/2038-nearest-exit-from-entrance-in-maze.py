from collections import deque
from typing import List

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(maze), len(maze[0])
        queue = deque([(entrance[0], entrance[1], 0)])  # (row, col, steps)
        visited = set()
        visited.add((entrance[0], entrance[1]))
        
        while queue:
            i, j, steps = queue.popleft()
            
            for dx, dy in moves:
                x, y = i + dx, j + dy
                
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited and maze[x][y] == '.':
                    if x == 0 or x == m-1 or y == 0 or y == n-1:
                        return steps + 1
                    
                    visited.add((x, y))
                    queue.append((x, y, steps + 1))
        
        return -1
