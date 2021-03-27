class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []
        final = []
        self.backtrack(res, candidates, 0, n, target, final)
        return final

    def backtrack(self, res, candidates, start, n, target, final):
        for i in range(start, n):
            if target == 0 and res not in final:
                final.append(res.copy())
            elif target > 0:
                candidate = candidates[i]
                res.append(candidate)
                self.backtrack(res, candidates, i, n, target - candidate, final)
                res.pop()
            else:
                return
