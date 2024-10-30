# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a=[]
        b=[]
        def fillStack(s,l):
            x=l
            while x:
                s.append(x)
                x=x.next 
        fillStack(a,l1)
        fillStack(b,l2)
        c=0
        ans=ListNode()
        while a or b:
            if a and b:
                x=a.pop()
                y=b.pop()
                v=(x.val+y.val+c)%10
                c=(x.val+y.val+c)//10
                ans.val=v
                p=ListNode()
                p.next=ans
                ans=p
            elif a:
                x=a.pop()
                v=(x.val+c)%10
                c=(x.val+c)//10
                ans.val=v
                p=ListNode()
                p.next=ans
                ans=p
            elif b:
                x=b.pop()
                v=(x.val+c)%10
                c=(x.val+c)//10
                ans.val=v
                p=ListNode()
                p.next=ans
                ans=p
        if c :
            ans.val=c
            return ans 
        else:
            return ans.next
