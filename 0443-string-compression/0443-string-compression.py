class Solution:
    def compress(self, chars: List[str]) -> int:

        # a high perfomance yet n sapce complexity approach 
        ans=Deque(chars)
        print(ans)
        s=0
        end=len(chars)-1
        curr=None
        c=0
        while s<=end:
        
            if not curr:
                curr=ans.pop()
                c=1
                s+=1
            while s<=end and ans[-1]==curr:
                ans.pop()
                c+=1
                s+=1
            if c!=1:
                c=str(c)
                for x in c[::-1]:
                    ans.appendleft(str(x))
            ans.appendleft(str(curr))
            curr=None
        chars[:]=list(ans)
        return len(ans)
        # end=lne(chars)
        # s=0
        # c=0
        # i=0
        # curr=None
        # while s<end:
        #     if not curr:
        #         curr=chars[i]
        #         c=1
        #     ci=i
        #     while char[i+1]==chars[i]:
        #         i+=1
        #         c+=1
        #     char=char[ci:i-1]
        #     if c!=1:
        #         c=str(c)
        #         for x in c[::-1]:
        #             char[i]

