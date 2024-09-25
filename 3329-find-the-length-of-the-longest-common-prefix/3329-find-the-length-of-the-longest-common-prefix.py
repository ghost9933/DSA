class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        ptree={}
        ans=0
        for num in arr2:
            root=ptree
            s=str(num)
            for i in s:
                if i not in root:
                    root[i]={}
                
                root=root[i]
                root['end2']=1
            root['end2']=1
        arr1=sorted(arr1,reverse=True)
        for num in arr1:
            c=0
            root=ptree
            s=str(num)
            if ans>len(s):
                break
            for i in s:
                if i in root and 'end2' in root[i]:
                    c+=1
                    print(c)
                else:
                    ans=max(c,ans)
                    break
                # if i not in root:
                #     root[i]={}
                root=root[i]
            ans=max(c,ans)
            root['end1']=1
            
        return ans

        print(ptree)
        print()