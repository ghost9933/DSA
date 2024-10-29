# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        x=head
        n=0
        while x:
            x=x.next
            n+=1
        print('len',n)
        isodd=False
        if n%2!=0:
            isodd=True
        if n==1:
            return True
        m=n//2
        print(m,'is odd',isodd)
        s=[]
        x=head
        for i in range(m):
            s.append(x.val)
            x=x.next
        print(s)
        print(x.val)
        if isodd:
            x=x.next
        print(x.val)
        while x:
            if x.val!=s[-1]:
                return False
            x=x.next
            s.pop()
        return True
    
        


