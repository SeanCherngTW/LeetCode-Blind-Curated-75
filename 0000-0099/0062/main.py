class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m_step = m - 1
        n_step = n - 1
        total_step = m_step + n_step
        return self.factorial(total_step) // (self.factorial(m_step) * self.factorial(n_step))

    def factorial(self, k):
        res = 1
        for i in range(1, k + 1):
            res *= i
        return res

    def uniquePathsDP(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        dp = [[1 for i in range(n)] for j in range(m)]

        for i in range(1, m):  # Skip 1st row since it's all 1
            for j in range(1, n):  # Skip 1st column since it's all 1
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]


s = Solution()
tests = [
    ((7, 3), 28),
    ((3, 3), 6),
]

for i, (x, y) in enumerate(tests):
    out = s.uniquePathsDP(*x)
    assert y == out, 'Test {}: Expect: {}, got {}'.format(i, y, out)

print('Example cases passed!')
