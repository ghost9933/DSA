from typing import List
from collections import defaultdict, deque

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        # Build the graph
        for u, v in connections:
            graph[u].append((v, 1))  # Original direction
            graph[v].append((u, 0))  # Reversed direction

        # BFS to count the changes needed
        queue = deque([0])
        visited = set()
        res = 0

        while queue:
            node = queue.popleft()
            visited.add(node)
            for neighbor, cost in graph[node]:
                if neighbor not in visited:
                    res += cost  # Count the change if it's in the original direction
                    queue.append(neighbor)

        return res
