# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a=headA

        b=headB
        n=set()
        while a!=None :
            if a not in n :
                n.add(a)
                a=a.next
            else :
                return(a)
        while b!=None :
            if b not in n :
                n.add(b)
                b=b.next
            else :
                return(b)

            