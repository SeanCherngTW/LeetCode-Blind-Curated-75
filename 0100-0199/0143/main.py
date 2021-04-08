# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        slow = head
        fast = head.next

        while fast.next and fast.next.next:
            # Make sure fast not None
            slow = slow.next
            fast = fast.next.next

        slow = slow.next  # 2nd list head
        if fast and fast.next:
            # For cases that fast.next.next is None
            # Make sure fast is the last node
            fast = fast.next

        # Reverse 2nd list
        pre = slow
        cur = slow.next
        pre.next = None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        # Zigzag
        cur = head
        while fast.next:  # Backword, fast is the last node
            tmp1 = cur.next
            tmp2 = fast.next
            cur.next = fast
            fast.next = tmp1
            cur = tmp1
            fast = tmp2

        return head
