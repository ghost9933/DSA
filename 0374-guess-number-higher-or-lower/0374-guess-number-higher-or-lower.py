# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        def guesser(s,e):
            m=(e-s)//2
            
            res=guess(s+m)
            print(m,res)
            if res==0:
                return s+m
            if res>0:
                return guesser(s+m+1,e)
            else:
                return guesser(s,s+m-1)
            
        return guesser(0,n)
