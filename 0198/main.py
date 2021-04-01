from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        res = dp[1]

        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
            res = max(res, dp[i])

        return res

    def robV2(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        slow = nums[0]
        fast = max(nums[0], nums[1])
        res = fast
        n = len(nums)

        for i in range(2, n):
            cur = max(slow + nums[i], fast)
            res = max(res, cur)
            slow = fast
            fast = cur

        return res


s = Solution()
tests = [
    ([1, 2, 3, 1], 4),
    ([2, 7, 9, 3, 1], 12),
    ([1], 1),
    ([2, 1], 2),
    ([10, 1, 1, 10], 20)
]

for i, (x, y) in enumerate(tests):
    out = s.robV2(x)
    assert y == out, 'Test {}: Expect: {}, got {}'.format(i, y, out)

print('Example cases passed!')
