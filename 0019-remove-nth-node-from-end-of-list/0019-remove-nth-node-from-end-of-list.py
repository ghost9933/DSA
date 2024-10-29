# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        e=head
        for i in range(n):
            e=e.next
        tbd=head
        p=None
        while e!=None:
            e=e.next
            p=tbd
            tbd=tbd.next
        if p:
            p.next=tbd.next
        else:
            return head.next
        return head