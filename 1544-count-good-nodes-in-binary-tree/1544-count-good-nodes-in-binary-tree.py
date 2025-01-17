# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans=0


    def trav(self,root,past):
        if root==None:
            return 
        
        if root.val>=past:
            past=max(root.val,past)
            self.ans+=1
            
        # print(path)
        self.trav(root.right,past)
        self.trav(root.left,past)

    def goodNodes(self, root: TreeNode) -> int:
        
        
        self.trav(root,root.val)
        return self.ans 
        