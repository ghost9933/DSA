class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals= sorted(intervals,key=lambda x:x[1])
        # print(intervals)
        ans=[]
        for x in intervals:
            # print(x,ans)
            if not ans:
                ans.append(x)
            else:
                if ans[-1][1]<=x[0]:
                    ans.append(x)
        return len(intervals)-len(ans)
        