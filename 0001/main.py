class Solution:
    from typing import List

    def twoSumV1(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSumV2(self, nums: List[int], target: int) -> List[int]:
        val_id_map = dict()
        for i, num in enumerate(nums):
            if num in val_id_map:
                return [val_id_map[num], i]
            else:
                val_id_map[target - num] = i


s = Solution()
assert(s.twoSumV2([2, 7, 11, 15], 9) == [0, 1])
assert(s.twoSumV2([3, 2, 4], 6) == [1, 2])
assert(s.twoSumV2([3, 3], 6) == [0, 1])
