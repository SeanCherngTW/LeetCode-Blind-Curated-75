class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [0] * len(nums)
        size = 0
        for num in nums:
            left, right = 0, size
            while left != right:
                mid = (left + right) // 2
                if res[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            res[left] = num
            size = max(left + 1, size)
        return size
