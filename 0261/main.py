from typing import List


class Solution:
    def isValidTree(self, nums: List[int]) -> int:
        graph = {}  # src: [des]
        rev_graph = {}  # des: [src]
        nodes = set()
        for src, des in nums:
            if des in rev_graph.keys():
                return False
            else:
                nodes.add(src)
                nodes.add(des)
                if src not in graph:
                    graph[src] = []
                graph[src].append(des)

                if des not in rev_graph:
                    rev_graph[des] = []
                rev_graph[des].append(src)
        root = None
        for des in graph:
            if des not in rev_graph:  # root
                if root:  # Duplicate root
                    return False
                else:
                    root = des
        if root is None:
            # cannot use "if not root" because it will be true if root == 0
            return False

        n = len(nodes)
        queue = [root]
        while queue:
            n -= 1
            src = queue.pop()
            if src in graph:
                des = graph[src]
                del graph[src]
                queue += des

        return n == 0


s = Solution()
tests = [
    ([[0, 1], [0, 2], [0, 3], [1, 4]], True),
    ([[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], False),
    ([[0, 1], [1, 2], [3, 4]], False)
]

for i, (x, y) in enumerate(tests):
    out = s.isValidTree(x)
    assert y == out, 'Test {}: Expect: {}, got {}'.format(i, y, out)

print('Example cases passed!')
