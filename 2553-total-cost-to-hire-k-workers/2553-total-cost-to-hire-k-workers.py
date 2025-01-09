class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n=len(costs)
        print('len is ',n)
        head=costs[:candidates]
        heapq.heapify(head)
        hp=candidates-1
        tp=n-candidates
        tail=costs[max(candidates, len(costs) - candidates):]
        heapq.heapify(tail)
        cost=0
        for i in range(k):
            # print(head,hp,'\t',tail,tp)
            if not tail or head  and  head[0]<=tail[0]:
                c=heapq.heappop(head)
                hp+=1
                if hp<tp:
                    heapq.heappush(head,costs[hp])
            else:
                c=heapq.heappop(tail)
                tp-=1
                if tp>hp:
                    heapq.heappush(tail,costs[tp])
            # print('selected cost',c)
            cost+=c
        return cost

        
