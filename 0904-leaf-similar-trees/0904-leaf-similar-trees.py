# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leftLeafs(tree,nodes):
            if not tree:
                
                return nodes
            elif tree.left==None and tree.right==None:
                print('leaf',tree)
                nodes.append(tree.val)
            else:
                nodes+=leftLeafs(tree.left,nodes[:])+leftLeafs(tree.right,nodes[:])
            return  nodes
        x=leftLeafs(root1,[])
        y=leftLeafs(root2,[])
        return x==y
