# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def add(l1, l2, carry) -> Optional[ListNode]:
            if not l1 and not l2:
                if carry == 0:
                    return None
                return ListNode(carry)
            if l1 and l2:
                sum = (l1.val + l2.val + carry)%10
                carry = (l1.val + l2.val + carry)//10
                return ListNode(sum, add(l1.next, l2.next, carry))
            elif l1 and not l2:
                return add(l1, ListNode(carry), 0)
            else:
                return add(ListNode(carry),l2, 0)
        return add(l1, l2, 0)