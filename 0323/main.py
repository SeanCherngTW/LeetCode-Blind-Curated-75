from typing import List


class Solution:
    def countComponentsBFS(self, edges: List[int]) -> int:
        graph = {}
        for src, des in edges:
            if src not in graph:
                graph[src] = []
            if des not in graph:
                graph[des] = []
            graph[src].append(des)
            graph[des].append(src)

        n = len(graph)
        visited = {}
        for node in graph:
            visited[node] = False

        nodes = list(graph.keys())
        queue = []
        res = 0
        for node in nodes:
            if not visited[node]:
                queue.append(node)
                while queue:
                    src = queue.pop()
                    visited[src] = True
                    for des in graph[src]:
                        if not visited[des]:
                            queue.append(des)
                res += 1

        return res

    def countComponentsDFS(self, edges: List[int]) -> int:
        graph = {}
        for src, des in edges:
            if src not in graph:
                graph[src] = []
            if des not in graph:
                graph[des] = []
            graph[src].append(des)
            graph[des].append(src)

        n = len(graph)
        visited = {}
        for node in graph:
            visited[node] = False

        nodes = list(graph.keys())
        queue = []
        res = 0
        for node in nodes:
            if not visited[node]:
                self.dfs(graph, node, visited)
                res += 1

        return res

    def dfs(self, graph, src, visited):
        if not visited[src]:
            visited[src] = True
            for des in graph[src]:
                self.dfs(graph, des, visited)


s = Solution()
tests = [
    ([[0, 1], [1, 2], [3, 4]], 2),
    ([[0, 1], [1, 2], [2, 3], [3, 4]], 1),
    ([[0, 1]], 1),
    ([], 0),
]

for i, (x, y) in enumerate(tests):
    out = s.countComponentsDFS(x)
    assert y == out, 'Test {}: Expect: {}, got {}'.format(i, y, out)
    out = s.countComponentsBFS(x)
    assert y == out, 'Test {}: Expect: {}, got {}'.format(i, y, out)

print('Example cases passed!')
