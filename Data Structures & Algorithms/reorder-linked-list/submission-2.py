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
        if not head or not head.next:
            return 
        def reverseList(head):
            if not head or not head.next:
                return head
            rest = reverseList(head.next)
            head.next.next = head
            head.next = None
            return rest
        def mergeList(list1, list2):
            if not list1 and not list2:
                return None
            elif not list1:
                return list2
            elif not list2:
                return list1
            temp = list1.next
            list1.next = list2
            list2.next = mergeList(temp, list2.next)
            return list1
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        prev.next = None
        list1 = head
        list2 = reverseList(slow)
        head =mergeList(list1, list2)