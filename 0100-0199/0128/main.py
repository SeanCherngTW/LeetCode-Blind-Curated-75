from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 1
        cur = 1
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 0:
                continue
            cur = cur + 1 if nums[i] - nums[i - 1] == 1 else 1
            res = max(res, cur)
        return res

    def longestConsecutiveNoSort(self, nums: List[int]) -> int:
        res = 0
        lengths = {}
        for num in nums:
            if num not in lengths:
                left_length = lengths.get(num - 1, 0)
                right_length = lengths.get(num + 1, 0)
                length = left_length + 1 + right_length
                res = max(res, length)
                lengths[num - left_length] = length
                lengths[num] = length
                lengths[num + right_length] = length
        return res


s = Solution()
tests = [
    ([1, 2, 0, 1], 3),
    ([100, 4, 200, 1, 3, 2], 4),
    ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
    ([], 0),
    ([1], 1),
    ([1, 3, 5, 7, 9, 1], 1),
]

for i, (x, y) in enumerate(tests):
    out = s.longestConsecutiveNoSort(x)
    assert y == out, 'Test {}: Expect: {}, got {}'.format(i, y, out)

print('Example cases passed!')
