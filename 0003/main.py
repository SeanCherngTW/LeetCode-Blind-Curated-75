class Solution:
    def lengthOfLongestSubstringV1(self, s: str) -> int:
        slow = 0
        fast = 0
        res = 0
        while fast < len(s):
            sub_str = s[slow:fast]
            if self.is_unique(sub_str):
                res = max(res, len(sub_str))
                fast += 1
            else:
                slow += 1
        return res

    def is_unique(self, sub_str: str):
        return len(set(sub_str)) == len(sub_str)

    def lengthOfLongestSubstringV2(self, s: str) -> int:
        slow = 0
        fast = 0
        res = 0
        char_set = set()
        for fast in range(len(s)):
            while s[fast] in char_set:
                # duplicate, remove slow
                char_set.remove(s[slow])
                slow += 1
            else:
                res = max(res, fast - slow + 1)
                char_set.add(s[fast])
        return res


s = Solution()
tests = [
    ('abcabcbb', 3),
    ('bbbbb', 1),
    ('pwwkew', 3),
]

for i, (x, y) in enumerate(tests):
    out = s.lengthOfLongestSubstringV2(x)
    assert y == out, 'Test {}: Expect: {}, got {}'.format(i, y, out)

print('Example cases passed!')
