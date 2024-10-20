class Solution:
    def compress(self, chars: List[str]) -> int:

        # a high perfomance yet n sapce complexity approach 
        # ans=Deque(chars)
        # print(ans)
        # s=0
        # end=len(chars)-1
        # curr=None
        # c=0
        # while s<=end:
        
        #     if not curr:
        #         curr=ans.pop()
        #         c=1
        #         s+=1
        #     while s<=end and ans[-1]==curr:
        #         ans.pop()
        #         c+=1
        #         s+=1
        #     if c!=1:
        #         c=str(c)
        #         for x in c[::-1]:
        #             ans.appendleft(str(x))
        #     ans.appendleft(str(curr))
        #     curr=None
        # chars[:]=list(ans)
        # return len(ans)

        # my code  a two pointer approach
        curr=chars[0]
        c=1
        i=0
        # j=0
        while i<len(chars):
            j=i+1
            while j<len(chars) and chars[i]==chars[j]:
                j+=1
            c=j-i
            # print('before ins',i,j,c)
            if c>1:
                c=str(c)
                for x in c:
                    chars[i+1]=x
                    i+=1
           
            if j==len(chars):
                chars[:]=chars[:i+1]
            else:
                chars[:]=chars[:i+1]+chars[j:]
            # print('after ins no',chars,i,j)
            i+=1

        return i

  