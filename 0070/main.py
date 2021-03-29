class Solution:
    def climbStairsV1(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2

        steps = [None] * (n + 1)
        steps[0] = 0
        steps[1] = 1
        steps[2] = 2

        for i in range(3, n + 1):
            steps[i] = steps[i - 2] + steps[i - 1]

        return steps[-1]

    def climbStairsV2(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2

        slow = 1
        fast = 2

        for i in range(3, n + 1):
            res = slow + fast
            slow = fast
            fast = res

        return res


s = Solution()
tests = [
    (2, 2),
    (3, 3)
]

for i, (x, y) in enumerate(tests):
    out = s.climbStairsV2(x)
    assert y == out, 'Test {}: Expect: {}, got {}'.format(i, y, out)

print('Example cases passed!')
