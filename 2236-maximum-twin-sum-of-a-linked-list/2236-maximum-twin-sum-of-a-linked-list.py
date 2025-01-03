# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack=[]
        f=head
        s=head
        while f and f.next:
            f=f.next.next
            stack.append(s.val)
            s=s.next
        ans=-math.inf
        while s:
            p=stack.pop()
            if s.val+p>ans:
                ans=s.val+p
            s=s.next
        return ans 


        