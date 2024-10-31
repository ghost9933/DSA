# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head :
            return None
        s=head
        f=head
        while f and f.next:
            s=s.next
            f=f.next.next
            
            if s==f:
                break
            
        
        if f==None or f.next==None:
            return None 
        f=head
        if f==s:
            return s
        while s!=f:
            s=s.next
            f=f.next
        return s
