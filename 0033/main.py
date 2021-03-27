from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Find pivot
        # All elements in pivot's left are larger than all elements in pivot's rignt
        n = len(nums)
        l, r = 0, n - 1
        while r > l:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:  # pivot in mid ~ r
                l = mid + 1
            else:  # pivot in l ~ mid
                r = mid

        min_idx = l
        pivot = n - min_idx
        l, r = 0, n - 1
        while r >= l:
            mid = (l + r) // 2
            real_mid = (mid - pivot) % n
            if nums[real_mid] > target:
                r = mid - 1
            elif nums[real_mid] < target:
                l = mid + 1
            else:
                return real_mid
        return -1


s = Solution()
tests = [
    (([4, 5, 6, 7, 0, 1, 2], 0), 4),
    (([4, 5, 6, 7, 0, 1, 2], 3), -1),
    (([1], 0), -1),
]

for i, (x, y) in enumerate(tests):
    out = s.search(*x)
    assert y == out, 'Test {}: Expect: {}, got {}'.format(i, y, out)

print('Example cases passed!')
