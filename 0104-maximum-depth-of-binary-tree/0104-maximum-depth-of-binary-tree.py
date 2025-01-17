# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def trav(self,root: Optional[TreeNode],c,map) -> int:
        if root!=None:
            if (root,root.left) in map:
                l=map[(root,root.left)]
            else :
                map[(root,root.left)]=self.trav(root.left,c+1,map)
                l=map[(root,root.left)]
            if (root,root.right) in map:
                r=map[(root,root.right)]
            else :
                map[(root,root.right)]=self.trav(root.right,c+1,map)
                r=map[(root,root.right)]
            return max(l,r)
        else :
            return c
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        map={}
        return self.trav(root,0,map)

