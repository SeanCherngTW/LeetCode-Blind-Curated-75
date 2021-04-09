from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        res = []
        for n in range(num + 1):
            res.append(self.countOnes(n))
        return res

    def countOnes(self, n):
        if n == 1:
            return 1
        ones = 0
        while n > 1:
            if n % 2 == 1:
                ones += 1
            n = n // 2
        ones = ones + 1 if n == 1 else ones
        return ones

    def countBitsV2(self, num: int) -> List[int]:
        res = [0] * (num + 1)
        offset = 1
        res[0] = 0
        for i in range(1, num + 1):
            if offset * 2 == i:
                offset *= 2
            res[i] = res[i - offset] + 1

        return res


s = Solution()
tests = [
    (2, [0, 1, 1]),
    (5, [0, 1, 1, 2, 1, 2]),
    (0, [0]),
]

for i, (x, y) in enumerate(tests):
    out = s.countBits(x)
    assert y == out, 'Test {}: Expect: {}, got {}'.format(i, y, out)

print('Example cases passed!')
