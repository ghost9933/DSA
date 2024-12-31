class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans=[]
        top=None
        for x in asteroids:
            ans.append(x)
            # print('loop for ',x,ans)
            if len(ans)>=2:
                
                while len(ans)>1 and ((ans[-2]>0 and ans[-1]<0) ):
                # or (ans[-2]<0 and ans[-1]>0)):
                    # print('collision detected ')
                    # print(ans)
                    a=ans.pop()
                    b=ans.pop()
                    # print('\t',a,b)
                    if a+b!=0:
                        if abs(a)>abs(b):
                            ans.append(a)
                        else:
                            ans.append(b)
        return ans 
                     
            