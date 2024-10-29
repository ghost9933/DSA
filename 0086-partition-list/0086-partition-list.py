# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None 
        s=ListNode()
        e=ListNode()
        ans1=s
        ans2=e
        n=head
        ps=None
        pe=None
        while n!=None:
            if n.val<x:
                s.val=n.val
                ps=s
                s.next=ListNode()
                s=s.next
            else:
                e.val=n.val
                pe=e
                e.next=ListNode()
                e=e.next
            n=n.next
        if ps:
            ps.next=None
        else :
            pe.next=None
            return ans2
        if pe:
            pe.next=None
        else :
            ps.next=None
            return ans1
        ps.next=ans2
        print(ans1)
        print(ans2)
        return ans1