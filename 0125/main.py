class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([c.lower() for c in s if c.isalpha() or c.isnumeric()])
        n = len(s)
        for i in range(n // 2):
            if s[i] != s[n - i - 1]:
                return False
        return True

    def isPalindromeInplace(self, s: str) -> bool:
        n = len(s)
        i = 0
        j = n - 1
        while i < j:
            while i < j and not self.isValid(s[i]):
                i += 1
            while i < j and not self.isValid(s[j]):
                j -= 1
            if self.isSame(s[i], s[j]):
                i += 1
                j -= 1
            else:
                return False
        return True

    def isValid(self, c):
        return c.isalpha() or c.isnumeric()

    def isSame(self, c1, c2):
        return c1.lower() == c2.lower()


s = Solution()
tests = [
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    ("0P", False),
    (",", True),
    ("A", True),
    (" ", True),
]

for i, (x, y) in enumerate(tests):
    out = s.isPalindromeInplace(x)
    assert y == out, 'Test {}: Expect: {}, got {}'.format(i, y, out)

print('Example cases passed!')
