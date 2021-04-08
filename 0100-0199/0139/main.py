from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for end in range(1, n + 1):
            for start in range(end):
                if dp[start] and s[start:end] in wordDict:
                    dp[end] = True
                    break
        return dp[n]


s = Solution()
tests = [
    (("applepenapple", ["apple", "pen"]), True),
    (("catsandog", ["cats", "dog", "sand", "and", "cat"]), False),
    (("", [""]), True),
    (("a", ["a"]), True),
]

for i, (x, y) in enumerate(tests):
    out = s.wordBreak(*x)
    assert y == out, 'Test {}: Expect: {}, got {}'.format(i, y, out)

print('Example cases passed!')
