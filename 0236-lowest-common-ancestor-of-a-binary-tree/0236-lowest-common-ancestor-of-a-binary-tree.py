# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans=[]
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        queue = [root]
        ans = []
        
        while queue:
            level_size = len(queue)
            level_vals = []
            
            for _ in range(level_size):
                node = queue.pop(0)
                level_vals.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            ans.append(level_vals[-1])
        
        return ans


