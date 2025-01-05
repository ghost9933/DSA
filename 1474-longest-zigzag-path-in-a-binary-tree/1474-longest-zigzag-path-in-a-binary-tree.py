# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ans=-math.inf
        def trav(dir,curr,l:int):
            nonlocal ans 
            if l>ans:
                ans=l
            if not dir:
                if curr.left:
                    trav('L',curr.left,l+1)
                if curr.right:
                    trav('R',curr.right,l+1)
            elif dir=='L':
                if curr.right:
                    trav('R',curr.right,l+1)
                if curr.left:
                    trav('L',curr.left,1)
            elif dir=='R' :
                if curr.left:
                    trav('L',curr.left,l+1)
                if curr.right:
                    trav('R',curr.right,1)
            return
        trav(None,root,0)
        return ans 
