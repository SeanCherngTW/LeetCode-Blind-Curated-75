class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict = {}
        for c in t:
            t_dict[c] = t_dict.get(c, 0) + 1
