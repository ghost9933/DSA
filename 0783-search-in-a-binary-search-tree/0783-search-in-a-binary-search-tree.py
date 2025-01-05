# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # print(root.val,root)
        if root is None or val == root.val:
            return root
        if root.val>val:
            # print('\t L')
            if root.left:
                x=self.searchBST(root.left, val)
                return x
            else:
                return None 
        else:
            # print('\t R')
            if root.right:
                x=self.searchBST(root.right, val)
                return x
            else:
                return None

