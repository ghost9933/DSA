from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n=len(rooms)
        q=deque()
        q.append(0)
        seen=set()
        while q:
            cr=q.popleft()
            seen.add(cr)
            for x in rooms[cr]:
                if x not in seen:
                    q.append(x)
        print(seen,n)
        if len(seen)<n:
            return False
        return True