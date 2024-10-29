# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x=l1
        y=l2
        c=0
        ans=ListNode()
        p=ans
        while x or y:
            if x and y:
                ans.val=(x.val+y.val+c)%10
                c=(x.val+y.val+c)//10
                if x.next or y.next or c!=0:
                    ans.next=ListNode()
                ans=ans.next
                x=x.next
                y=y.next
            elif x:
                ans.val=(x.val+c)%10
                c=(x.val+c)//10
                if x.next or c!=0:
                    ans.next=ListNode()
                ans=ans.next
                x=x.next
            elif y:
                ans.val=(y.val+c)%10
                c=(y.val+c)//10
                if y.next or c!=0:
                    ans.next=ListNode()
                ans=ans.next
                y=y.next
            elif c>0:
                ans.val=c
            else:
                return p
        if c!=0:
            ans.val=c
        return p


