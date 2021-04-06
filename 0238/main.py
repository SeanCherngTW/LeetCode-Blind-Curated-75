class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        product = 1
        zeros = 0
        zero_idx = None
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                zeros += 1
                zero_idx = i
            else:
                product *= nums[i]

        if zeros == 1:
            res = [0] * n
            res[zero_idx] = product
            return res
        if zeros >= 2:
            return [0] * n

        res = []
        for i in range(n):
            res.append(product // nums[i])

        return res

    def productExceptSelfNoDiv(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        n = len(nums)
        res = [1] * n
        product = 1
        for i in range(n):
            # Multiple numbers on left hand side
            res[i] = product
            product *= nums[i]

        product = 1
        for i in range(n - 1, -1, -1):
            # Multiple numbers on right hand side
            res[i] *= product
            product *= nums[i]

        return res
