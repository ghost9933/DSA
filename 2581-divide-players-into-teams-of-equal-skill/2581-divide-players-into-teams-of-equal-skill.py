class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # print(sum(skill))
        if sum(skill)%(len(skill)/2)!=0:
            return -1
        target=(sum(skill)/(len(skill)/2))
        pairs=[]
        map=dict(Counter(skill))
        # print(map)
        pairs=[]
        for x in skill:
            if target-x in map and map[target-x]>=1 and map[x]>=1:
                map[target-x]-=1
                map[x]-=1
                pairs.append((x,int(target-x)))
                # print('updated map',map)
        # print(pairs)
        if len(pairs)!=len(skill)//2:
            return -1
        ans=0
        for x in pairs:
            ans+=x[0]*x[1]
        # print(ans)
        if ans==0:
            return -1
        return ans 


                
        
        