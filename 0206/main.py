# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        pre = None
        cur = head

        while cur:
            _next = cur.next
            cur.next = pre
            pre = cur
            cur = _next

        return pre

        # Version 2
        # while cur and cur.next:
        #     _next = cur.next
        #     cur.next = pre
        #     pre = cur
        #     cur = _next

        # return cur
