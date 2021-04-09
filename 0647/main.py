class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = n  # at least n palindromic (with len = 1)
        for size in range(1, n):
            for i in range(0, n - size, size):
                j = i + size
                if self.isPalindromic(s[i:j + 1]):
                    res += 1
        return res

    def isPalindromic(self, s):
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def countSubstringsDP(self, s: str) -> int:
        n = len(s)
        res = 0
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    res += 1
                else:
                    dp[i][j] = False
        return res
