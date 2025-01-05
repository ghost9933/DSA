# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q=deque()
        q.append(root)
        ans=-math.inf
        l=None
        cl=1
        while q:
            n=len(q)
            lsum=0
    
            for i in range(n):
                c=q.popleft()
                if c:
                    lsum+=c.val
                    if c.left:
                        q.append(c.left)
                    if c.right:
                        q.append(c.right)
            if lsum>ans:
                ans=lsum
                l=cl
            cl+=1
        return l 
