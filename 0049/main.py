class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for _str in strs:
            key = ''.join(sorted(_str))
            if key in res:
                res[key].append(_str)
            else:
                res[key] = [_str]

        return res.values()
