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

        # my code 
        curr=chars[0]
        c=1
        i=0
        j=0
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
        chars[:] = chars[:i]
        return i

        # # chatgpt
        # write = 0  # Pointer to write position
        # read = 0   # Pointer to read position
        
        # while read < len(chars):
        #     curr_char = chars[read]
        #     count = 0
            
        #     # Count occurrences of the current character
        #     while read < len(chars) and chars[read] == curr_char:
        #         read += 1
        #         count += 1
            
        #     # Write the character
        #     chars[write] = curr_char
        #     write += 1
            
        #     # If more than 1 occurrence, write the count
        #     if count > 1:
        #         for digit in str(count):
        #             chars[write] = digit
        #             write += 1
        
        # return write  # New length of the list

        

