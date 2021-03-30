from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1  # width
        area = 0
        while i < j:
            left = height[i]
            right = height[j]
            area = max(area, (j - i) * min(left, right))
            if left > right:
                j -= 1
            else:
                i += 1
        return area


s = Solution()
tests = [
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
    ([1, 1], 1),
    ([4, 3, 2, 1, 4], 16),
    ([1, 2, 1], 2),
]

for i, (x, y) in enumerate(tests):
    out = s.maxArea(x)
    assert y == out, 'Test {}: Expect: {}, got {}'.format(i, y, out)

print('Example cases passed!')
