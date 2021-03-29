from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        res = []
        for cur in sorted(intervals, key=lambda interval: interval[0]):
            if res:
                if cur[0] <= res[-1][1]:
                    res[-1][1] = max(cur[1], res[-1][1])
                else:
                    res.append(cur)
            else:
                res.append(cur)

        return res


s = Solution()
tests = [
    ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
    ([[1, 4], [4, 5]], [[1, 5]]),
    ([[0]], [[0]]),
    ([], []),
    ([[1, 4], [2, 3]], [[1, 4]]),
    ([[1, 1], [1, 1], [1, 1], [1, 1]], [[1, 1]]),
]

for i, (x, y) in enumerate(tests):
    out = s.merge(x)
    assert y == out, 'Test {}: Expect: {}, got {}'.format(i, y, out)

print('Example cases passed!')
