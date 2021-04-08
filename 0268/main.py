class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        res = [0] * n
        for num in nums:
            res[num] = 1
        return res.index(0)

    def missingNumberV2(self, nums: List[int]) -> int:
        n = len(nums)
        res = n * (1 + n) // 2
        for num in nums:
            res -= num
        return res
