class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res=0
        c=0
        for a in gain:
            c+=a
            res=max(res,c)
        return res
