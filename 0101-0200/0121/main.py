from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        cur = 0
        for i in range(1, len(prices)):
            cur += prices[i] - prices[i - 1]
            res = max(res, cur)
            cur = max(cur, 0)
        return res


s = Solution()
tests = [
    ([7, 1, 5, 3, 6, 4], 5),
    ([7, 6, 4, 3, 1], 0),
    ([7, 5, 4, 3, 1, 2], 1),
]

for i, (x, y) in enumerate(tests):
    out = s.maxProfit(x)
    assert y == out, 'Test {}: Expect: {}, got {}'.format(i, y, out)

print('Example cases passed!')
