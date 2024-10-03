class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target=dict(Counter(p))
        # print(target)
        lenTarget=len(p)
        window={}
        ans=[]
        for i in range (len(s)):
            
            # print(i,window)
            entering=s[i]
            if entering in window:
                window[entering]+=1
            else:
                window[entering]=1
            if i<lenTarget:
                exiting=None 
            else:
                exiting=s[i-lenTarget]
            # print(entering,exiting)

            if exiting:
                window[exiting]-=1
                if window[exiting]==0:
                    del window[exiting]
            # print(i, 'target',target,'\t current window',window)
            if window==target:
                # print('added at',i)
                ans.append(i-lenTarget+1)
        return ans 


