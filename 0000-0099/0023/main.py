class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MinPriorityQueue:
    def __init__(self):
        # Heap index start from 1
        # So the the parent & child indexing will be correct
        self.heap = [None]
        self.length = 0

    def insert(self, node):
        self.heap.append(node)
        self.length += 1
        self.__swim(self.length)

    def pop(self):
        if self.length == 0:
            return
        self.__swap(1, self.length)
        self.length -= 1
        min_node = self.heap.pop()
        self.__sink(1)
        return min_node

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __swim(self, i):
        # Move button to root
        while i > 1 and self.heap[i].val < self.heap[i // 2].val:
            j = i // 2  # j = Parent
            self.__swap(i, j)
            i = j

    def __sink(self, i):
        # Move root to button
        while i * 2 <= self.length:
            j = i * 2  # j = Left child

            # SHOULD COMPARE WHICH CHILD IS SMALLER
            if j < self.length and self.heap[j].val > self.heap[j + 1].val:
                j += 1  # Right child exists and smaller than left child

            if self.heap[j].val < self.heap[i].val:
                self.__swap(i, j)
                i = j
            else:
                break


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        pass
        res = ListNode(0)
        pCur = res
        num_lists = len(lists)
        finished_lists = 0
        min_priority_queue = MinPriorityQueue()

        for head in lists:
            if head:
                min_priority_queue.insert(head)

        while min_priority_queue.length > 0:
            node = min_priority_queue.pop()
            pCur.next = node
            pCur = pCur.next
            node = node.next

            if node:
                min_priority_queue.insert(node)

        return res.next
