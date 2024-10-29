# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def add(l1: Optional[ListNode], l2: Optional[ListNode], carry: int) -> Optional[ListNode]:
            if not l1 and not l2:
                if carry == 0:
                    return None
                else:
                    return ListNode(carry)
            
            if not l2:
                if carry == 0:
                    return l1
                else:
                    sum_value = l1.val + carry
                    l1.val = sum_value % 10
                    carry = sum_value // 10
                    l1.next = add(l1.next, None, carry)
                    return l1

            if not l1:
                if carry == 0:
                    return l2
                else:
                    sum_value = l2.val + carry
                    l2.val = sum_value % 10
                    carry = sum_value // 10
                    l2.next = add(l2.next, None, carry)
                    return l2
            
            sum_value = l1.val + l2.val + carry
            result_node = ListNode(sum_value % 10)
            carry = sum_value // 10
            result_node.next = add(l1.next, l2.next, carry)
            return result_node
        return add(l1, l2, 0)