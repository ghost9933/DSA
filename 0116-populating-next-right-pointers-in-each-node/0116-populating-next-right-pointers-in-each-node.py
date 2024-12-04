"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def trav(self,root, parrent,c):

        if not root :
            return
        
        if parrent and c=='L':
            root.next=parrent.right
        elif parrent  and c=='R' and parrent.next:
            root.next=parrent.next.left
        else:
            root.next=None
        # print(root.val,'next',root.next) 
        if root.left:
            self.trav(root.left,root,'L')
        if root.right:
            self.trav(root.right,root,'R')
    def inorder(self,root):
        if not root:
            return
        print('Node',root.val)
        if root.next:
            print('\t next is',root.next.val)
        else:
            print('next is null')
        print('***'*10) 
        if root.left:
            self.inorder(root.left)
       
        if root.right:
            self.inorder(root.right)

        

    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        self.trav(root,None,None)
        # self.inorder(root)
        return root

        