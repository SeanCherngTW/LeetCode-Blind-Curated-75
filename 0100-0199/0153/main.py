from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        while l < r:
            m = (l + r) // 2
            if m > 0 and nums[m] < nums[m - 1]:
                return nums[m]
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1

        return nums[l]


"""
4 5 6 7 0 1 2
l     m     r
        l m r
        r
        l

0 1 2 4 5 6 7
l     m     r
l m r

1 2 4 5 6 7 0
l     m     r
        l m r
            l

3 1 2
l m r
r
l
"""

s = Solution()
tests = [
    ([4, 5, 6, 7, 0, 1, 2], 0),
    ([3, 4, 5, 1, 2], 1),
    ([11, 13, 15, 17], 11),
]

for i, (x, y) in enumerate(tests):
    out = s.findMin(x)
    assert y == out, 'Test {}: Expect: {}, got {}'.format(i, y, out)

print('Example cases passed!')
