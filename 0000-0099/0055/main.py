class Solution:
    def canJumpBackTrack_TLE(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        cur = 0
        return self.jump(nums, cur, nums[0], goal)

    def jump(self, nums, cur, steps, goal):
        if cur == goal:
            return True
        elif cur > goal:
            return False
        else:
            res = False
            for step in range(1, steps + 1):
                if cur + step <= goal:
                    cur += step
                    res = self.jump(nums, cur, nums[cur], goal)
                    cur -= step
                if res:
                    return True
            return res

    def canJumpLinear(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        res = 0
        i = 0

        while i <= n and i <= res:
            res = max(res, nums[i] + i)
            if res >= n:
                return True
            i += 1

        return False
