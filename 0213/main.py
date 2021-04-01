from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        n = len(nums)
        dp0 = [0] * n
        dp1 = [0] * n

        dp0[0] = nums[0]
        dp0[1] = dp0[0]

        dp1[0] = 0
        dp1[1] = nums[1]

        res = max(dp0[2], dp1[2])

        for i in range(2, n):
            if i != n - 1:  # Not the last element
                dp0[i] = max(dp0[i - 2] + nums[i], dp0[i - 1])
            dp1[i] = max(dp1[i - 2] + nums[i], dp1[i - 1])
            res = max(res, dp0[i], dp1[i])

        return res


s = Solution()
tests = [
    ([2, 3, 2], 3),
    ([1, 2, 3, 1], 4),
    ([1, 2], 2),
    ([4, 1, 2, 7, 5, 3, 1], 14),
]

for i, (x, y) in enumerate(tests):
    out = s.rob(x)
    assert y == out, 'Test {}: Expect: {}, got {}'.format(i, y, out)

print('Example cases passed!')
