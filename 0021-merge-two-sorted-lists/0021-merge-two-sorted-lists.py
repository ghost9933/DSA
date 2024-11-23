# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1=list1
        l2=list2
        # print(l1,l2)
        start=ListNode()
        current=ListNode()
        s=1
        if l1==None:
            return l2
        if l2==None:
            return l1

        if l1==None and l2==None:
                return start.next
        while l1!=None and l2!=None:
            

            x=ListNode()
            if l1.val<=l2.val:
                x.val=l1.val
                l1=l1.next
            else :
                x.val=l2.val
                l2=l2.next
            if s==1:
                start=x
                current=start
                s=0
            else :
                current.next=x
                current=current.next
            # print(start)
        if l1==None and l2!=None:
            current.next=l2
        if l2==None and l1!=None:
            current.next=l1
        return start
        