from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses < 2:
            return True

        graph = {}
        num_pre = [0] * numCourses
        for course, pre in prerequisites:
            if pre in graph:
                graph[pre].append(course)
            else:
                graph[pre] = [course]
            num_pre[course] += 1

        queue = []
        finished = 0
        for i in range(numCourses):
            if num_pre[i] == 0:
                finished += 1
                queue.append(i)

        while queue:
            pre = queue.pop(0)
            if pre in graph:
                for course in graph[pre]:
                    num_pre[course] -= 1
                    if num_pre[course] == 0:
                        finished += 1
                        queue.append(course)

        return finished == numCourses


s = Solution()
tests = [
    ((5, [[1, 4], [2, 4], [3, 1], [3, 2]]), True),
]

for i, (x, y) in enumerate(tests):
    out = s.canFinish(*x)
    assert y == out, 'Test {}: Expect: {}, got {}'.format(i, y, out)

print('Example cases passed!')
