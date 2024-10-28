# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        seen=set()
        duplicates=set()
        x=head
        while x!=None  :
            if x.val not in seen:
                seen.add(x.val)
            else :
                duplicates.add(x.val)
            x=x.next
        # print(duplicates)

        p=None
        c=head
        while c!=None :
            # print(c.val)
            if c.val  in duplicates:
                if c==head:
                    head=head.next
                    c=c.next
                else:
                    p.next=c.next
                    c=c.next
            else:
                p=c
                c=c.next


        # print(head)
        return head
