class Solution:
    memo=dict()
    def uniquePaths(self, m: int, n: int) -> int:
        if m==1 and n==1:
            return 1
        if m==2 and n==2:
            return 2
        if m==1 or n==1:
            return 1
        else:
            if tuple([m,n]) in self.memo:
                return self.memo[tuple([m,n])]
            else:
                self.memo[tuple([m,n])]=self.uniquePaths( m-1, n)+self.uniquePaths( m, n-1)
                return self.memo[tuple([m,n])]

