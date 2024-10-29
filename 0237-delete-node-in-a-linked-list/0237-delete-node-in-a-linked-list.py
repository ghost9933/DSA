# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        x=node
        p=None
        while x.next!=None:
            p=x
            x.val=x.next.val
            x=x.next
        x=None 
        p.next=None