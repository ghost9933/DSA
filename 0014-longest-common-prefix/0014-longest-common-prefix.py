class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        subseq=min(strs)
        strs.remove(subseq)
        for x in strs:
            
            strl=len(x)
            subl=len(subseq)
            print(strl,subl)
            for i in range(min(strl,subl)):
                print(i,subseq,x)
                if x[i]==subseq[i]:
                    continue 
                else:
                    subseq=x[:i]
                    break
            subseq=subseq[:len(min(strs))]
        return(str(subseq))