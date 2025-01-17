class Solution:
    def reverseWords(self, s: str) -> str:
        word=''
        ans=[]
        output=''
        for i in range(len(s)):
            
            if s[i]!=' ':
                word+=s[i]
                if i==len(s)-1:
                    ans.append(word)
            else:
                if word!='':
                    ans.append(word)
                    word=''
        while ans:
            if len(ans)==1:
                output+=ans.pop()
            else:
                output+=ans.pop()+' '
        return output