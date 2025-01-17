class Solution:
    def decodeString(self, s: str) -> str:
        
        stack=[]
        for i in range(len(s)):
            if s[i]!=']':
                stack.append(s[i])
                # print('a')
            else:
                decoded=''
                while len(stack)>0 and stack[-1]!='[':
                    decoded=''.join(stack.pop())+decoded
                    # print('b')
                if stack and stack[-1]=='[':
                    stack.pop()
                # count=1
                # mc=1
                # mul=0
                # while stack and stack[-1].isdigit():
                #     print('c')
                #     count=count*(mc*10**mul)+int(stack[-1])
                #     mul+=1
                #     mc+=1
                count = 0
                base = 1
                # Get the number k
                while stack and stack[-1].isdigit():
                    count = count + int(stack.pop()) * base
                    base *= 10
                
                n_decode = decoded * count  # Repeat the decoded string 'count' times
                # stack.append(n_decode) 
                stack.append(n_decode)
            print(stack)
        return ''.join(stack)


                