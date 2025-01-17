class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        lcs = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]
        print(lcs)
        for i in range(1,len(text1)+1):
            for j in range(1,len(text2)+1):
                # print('\n')
                # print(i,j)
            
                # for x in lcs:
                    # print(x)
                
                if text1[i-1]==text2[j-1]:
                    lcs[i][j]=int(lcs[i-1][j-1])+1
                    # print('same')
                else :
                    # print('not same')
                    # print(j-1,i,"\t",j,i-1)
                    a=lcs[i][j-1]
                    b=lcs[i-1][j]
                    lcs[i][j]=max(a,b)
        return lcs[-1][-1]