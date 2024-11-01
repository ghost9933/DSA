class MinStack:

    def __init__(self):
        self.stack=[]
        self.minS=[]


    def push(self, val: int) -> None:
        # print('push',val,self.stack)
        if not self.minS or self.minS[-1]>=val:
            self.minS.append(val)
        self.stack.append(val)
        

    def pop(self) -> None:
        r=self.stack[-1]
        if self.minS and self.minS[-1]==r:
            self.minS.pop()
        # print('poping\n',self.stack,'\n',self.stack[:-1])
        self.stack=self.stack[:-1]
        # return r
        

    def top(self) -> int:
        # print("top",self.stack[-1])
        return self.stack[-1]

    def getMin(self) -> int:
        # print("min",self.minS)
        if not self.minS:
            return
        return self.minS[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()