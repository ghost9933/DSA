class Solution:
    def minLength(self, s: str) -> int:
        
        # c=0
        # e=len(s)
        # while c<e-1:
        #     cur=s[c:c+2]
        #     # print(c,cur)
        #     if cur in {'AB','CD'}:
        #         if c+2<e:
        #             s=s[:c]+s[c+2:]
        #         else:
        #             s=s[:c]
        #         # print('new',s)
        #         c=max(c-2,0)
        #     else:
        #         c+=1
        # return len(s)

        # using stack
        stack=[]
        for  char in s:
            if not stack:
                stack.append(char)
            else:
                if stack[-1]+char in {'AB','CD'}:
                    stack.pop()
                else:
                    stack.append(char)
        return len(stack)
        