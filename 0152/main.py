from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        _max = _min = res = nums[0]

        for i in range(1, n):
            if nums[i] < 0:
                _max, _min = _min, _max

            tmp_max = _max
            _max = max(nums[i], nums[i] * _max, nums[i] * _min)
            _min = min(nums[i], nums[i] * _min, nums[i] * tmp_max)

            res = max(_max, res)

        return res


s = Solution()
tests = [
    ([2, 3, -2, 4], 6),
    ([-2, 0, -1], 0),
    ([2, 3, -2, -4], 48),
    ([-2, -3, -2, -4], 48),
    ([-2, 3, -2, -4], 24),
]

for i, (x, y) in enumerate(tests):
    out = s.maxProduct(x)
    assert y == out, 'Test {}: Expect: {}, got {}'.format(i, y, out)

print('Example cases passed!')
