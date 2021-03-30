class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)

        while i < n:
            if intervals[i][0] > newInterval[0]:
                intervals.insert(i, newInterval)
                break
            i += 1

        if n == 0 or i == n:  # insert to tail
            intervals.append(newInterval)

        for cur in intervals:
            if res:
                if cur[0] <= res[-1][1]:
                    res[-1][1] = max(res[-1][1], cur[1])
                else:
                    res.append(cur)
            else:
                res.append(cur)

        return res
