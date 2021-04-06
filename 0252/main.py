from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List) -> bool:
        if len(intervals) <= 1:
            return True
        intervals = sorted(intervals, key=lambda x: x[0])
        for i in range(1, len(intervals)):
            if intervals[i - 1][1] >= intervals[i][0]:
                # overlap
                return False
        return True


s = Solution()
tests = [
    ([[0, 30], [5, 10], [15, 20]], False),
    ([[7, 10], [2, 4]], True),
    ([[0, 1]], True),
    ([], True),
    ([[0, 3], [3, 6], [7, 8]], False),
]

for i, (x, y) in enumerate(tests):
    out = s.canAttendMeetings(x)
    assert y == out, 'Test {}: Expect: {}, got {}'.format(i, y, out)

print('Example cases passed!')
