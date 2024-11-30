class HitCounter:

    def __init__(self):
        self.stack=[]

    def hit(self, timestamp: int) -> None:
        self.stack.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        i=-1
        c=0
        n=len(self.stack)
        
        while  n+i>=0 and 300>timestamp-self.stack[i] :
            print(i, timestamp-self.stack[i] )
            c+=1
            i-=1
        return c

        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)