class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num)<=k:
            return '0'
        stack=[]
        for char in num:
            while stack and  k>0 and int(char)<int(stack[-1]):
                stack.pop()
                k-=1
            stack.append(char)
        stack = stack[:-k] if k else stack
        # print(stack)
        # if len(stack)==0 :
        #     return '0'
        return ''.join(stack).lstrip('0') or "0"
        