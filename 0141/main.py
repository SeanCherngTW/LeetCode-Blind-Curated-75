# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False

        node = head
        nodes = set()

        while node:
            if node in nodes:
                return True
            else:
                nodes.add(node)
                node = node.next

        return False

    def hasCycleInplace(self, head: ListNode) -> bool:
        if not head:
            return False

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
