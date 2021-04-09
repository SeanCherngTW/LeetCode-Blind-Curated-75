class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[1])
        res = 0
        last_end = float('-inf')
        for start, end in intervals:
            if start >= last_end:
                last_end = end
            else:
                res += 1
        return res
