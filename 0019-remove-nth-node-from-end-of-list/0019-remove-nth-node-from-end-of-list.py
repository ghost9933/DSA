# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tbd=end=head
        for i in range(n):
            end=end.next
        # print(tbd,end)
        prev=None
        while end!=None:
            prev=tbd
            tbd=tbd.next
            end=end.next
        # print(tbd,end)

        if prev==None:
            return tbd.next

        if tbd!=None:
            prev.next=tbd.next
        else:
            return None
        
        return head

