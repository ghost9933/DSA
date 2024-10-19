class Solution:
    #recursive approach 
    def levdistance(self,x,xl,y,yl):
        if xl==0:
            return yl
        if yl==0:
            return xl
        cost =0 if x[xl-1]==y[yl-1] else 1
        # print(x[:xl],"\n",y[:yl],"\n",cost,"\n","NEW recursion")
        return min(self.levdistance(x,xl-1,y,yl)+1,self.levdistance(x,xl,y,yl-1)+1,self.levdistance(x,xl-1,y,yl-1)+cost)



    def minDistance(self, word1: str, word2: str) -> int:
        n=len(word1)
        m=len(word2)
        map = [[0 for i in range(n + 1)] for y in range(m + 1)]
        
        for i in range(m+1):
            map[i][0]=i
        for j in range(n+1):
            map[0][j]=j
        print(map)
        cost=0
        for i in range(1,m+1):
            c=0
            for j  in range(1,n+1):
                c=0 if word1[j-1]==word2[i-1] else 1
                map[i][j]=min(map[i-1][j]+1,map[i][j-1]+1,map[i-1][j-1]+c)
        
        print(map)  
        return(map[m][n])             
