# class Solution:
#     def numberOfWays(self, s: str, t: str, k: int) -> int:
#         ans=0
#         n=len(s)
#         print(1,n-1)
#         print(s[0:]+s[:0])
#         print(s[n-1:]+s[:n-1])
#         def backtrack(inString,steps):
#             print(inString,steps)
#             nonlocal ans 
#             nonlocal n
#             if steps>k  :
#                 # or (inString==s and steps>0)
#                 return
#             if inString==t and steps<=k:
#                 print('found')
#                 ans+=1
             
            
#             for i in range (1,n-1):
#                 newString=inString[i:]+inString[:i]
#                 # if newString==s:
#                 #     ans+=1
#                 print(steps,'break  at',i)
#                 backtrack(inString[i:]+inString[:i],steps+1)
#         backtrack(s,0)
#         return  ans 

# class Solution:
#     def kmp(self, s, t):
#         pi, res = [0 for i in range(len(t))], []
#         for i in range(1, len(t)):
#             j = pi[i-1]
#             while j > 0 and t[j] != t[i]: j = pi[j-1]
#             pi[i] = 0 if j == 0 and t[0] != t[i] else j + 1
#         m, n, j = len(s), len(t), 0
#         for i in range(m):
#             while j >= n or j > 0 and s[i] != t[j]: j = pi[j-1]
#             if s[i] == t[j]: j += 1
#             if j == n: res.append(i - n + 1)
#         return res
#     def numberOfWays(self, s: str, t: str, k: int) -> int:
#         n, M = len(s), 10**9 + 7
#         pos = self.kmp((s+s)[:-1], t)
#         f_k = [0, 0]
#         f_k[1] = (pow(n-1, k, M) - (-1)**k + M) * pow(n, M-2, M) % M
#         f_k[0] = (f_k[1] + (-1)**k + M) % M
#         return sum(f_k[not not p] for p in pos) % M


class Solution:
    def kmp(self, s, t):
        pi, res = [0 for i in range(len(t))], []
        for i in range(1, len(t)):
            j = pi[i-1]
            while j > 0 and t[j] != t[i]: j = pi[j-1]
            pi[i] = 0 if j == 0 and t[0] != t[i] else j + 1
        m, n, j = len(s), len(t), 0
        for i in range(m):
            while j >= n or j > 0 and s[i] != t[j]: j = pi[j-1]
            if s[i] == t[j]: j += 1
            if j == n: res.append(i - n + 1)
        return res
    def numberOfWays(self, s: str, t: str, k: int) -> int:
        n, M = len(s), 10**9 + 7
        pos = self.kmp((s+s)[:-1], t)
        f_k = [0, 0]
        f_k[1] = (pow(n-1, k, M) - (-1)**k + M) * pow(n, M-2, M) % M
        f_k[0] = (f_k[1] + (-1)**k + M) % M
        return sum(f_k[not not p] for p in pos) % M