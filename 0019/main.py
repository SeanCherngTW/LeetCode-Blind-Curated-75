class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEndV1(self, head: ListNode, n: int) -> ListNode:
        total = 0
        pCur = head
        while pCur:  # Count number of nodes
            total += 1
            pCur = pCur.next

        target = total - n
        pCur = head
        if target == 0:
            return head.next
        else:
            for i in range(target):
                pPre = pCur
                pCur = pCur.next
            pPre.next = pCur.next
            return head

    def removeNthFromEndV2(self, head: ListNode, n: int) -> ListNode:
        node = ListNode(0)
        node.next = head
        fast = slow = node

        for i in range(n):
            fast = fast.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next

        return node.next
