class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [None] * n
        dp[0] = nums[0]
        res = nums[0]

        for i in range(1, n):
            dp[i] = nums[i] + max(dp[i - 1], 0)
            res = max(res, dp[i])

        return res
