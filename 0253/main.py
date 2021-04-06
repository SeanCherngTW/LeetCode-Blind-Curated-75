from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List) -> bool:
        intervals = sorted(intervals, key=lambda x: x[0])
        if len(intervals) <= 1:
            return len(intervals)
        rooms = [intervals[0][1]]
        for interval in intervals[1:]:
            cur_start, cur_end = interval

            is_arranged = False
            for i in range(len(rooms)):
                if rooms[i] < cur_start:
                    rooms[i] = cur_end
                    is_arranged = True

            if not is_arranged:
                rooms.append(cur_end)
        return len(rooms)


s = Solution()
tests = [
    ([[0, 30], [5, 10], [15, 20]], 2),
    ([[7, 10], [2, 4]], 1),
    ([[0, 1]], 1),
    ([], 0),
    ([[0, 3], [3, 6], [7, 8]], 2),
    ([[0, 1], [0, 1], [0, 1], [0, 2], [0, 3]], 5),
    ([[0, 1], [0, 1], [0, 1], [1, 2], [2, 3]], 4),
]

for i, (x, y) in enumerate(tests):
    out = s.minMeetingRooms(x)
    assert y == out, 'Test {}: Expect: {}, got {}'.format(i, y, out)

print('Example cases passed!')
