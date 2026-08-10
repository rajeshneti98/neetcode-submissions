# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def merge(head1, head2):
            if not head1:
                return head2
            elif not head2:
                return head1
            temp1 = head1.next
            temp2 = head2.next
            head1.next = head2
            head2.next = merge(temp1, temp2)
            return head1
        slow, fast, tail1 = head, head, None
        count = 0
        while slow and fast:
            tail1 = slow
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next

        tail1.next = None
        prev, curr = None, slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        merge(head, prev)
        