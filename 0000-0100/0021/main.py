class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        pass
        head = ListNode(0)  # Dummy
        pCur = head

        while l1 and l2:
            if l1.val < l2.val:
                pCur.next = l1
                l1 = l1.next
            else:
                pCur.next = l2
                l2 = l2.next
            pCur = pCur.next

        while l1:
            pCur.next = l1
            pCur = pCur.next
            l1 = l1.next

        while l2:
            pCur.next = l2
            pCur = pCur.next
            l2 = l2.next

        return head.next
