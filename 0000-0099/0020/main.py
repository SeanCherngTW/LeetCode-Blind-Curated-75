class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left = ['(', '[', '{']
        right = [')', ']', '}']
        for c in s:
            if c in left:
                stack.append(c)
            else:
                if not stack:
                    return False
                out = stack.pop()
                if out == '(' and c == ')':
                    pass
                elif out == '[' and c == ']':
                    pass
                elif out == '{' and c == '}':
                    pass
                else:
                    return False
        return not stack


s = Solution()
tests = [
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
    ("([)]", False),
    ("{[]}", True),
]

for i, (x, y) in enumerate(tests):
    out = s.isValid(x)
    assert y == out, 'Test {}: Expect: {}, got {}'.format(i, y, out)

print('Example cases passed!')
