from typing import List


class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for r in range(n // 2):  # round
            for i in range(r, n - 1 - r):
                # Up to Right
                matrix[r][i], matrix[i][n - 1 - r] = matrix[i][n - 1 - r], matrix[r][i]

                # Right to Down
                matrix[r][i], matrix[n - 1 - r][n - 1 - i] = matrix[n - 1 - r][n - 1 - i], matrix[r][i]

                # Down to Left
                matrix[r][i], matrix[n - 1 - i][r] = matrix[n - 1 - i][r], matrix[r][i]
        return matrix


s = Solution()
tests = [
    ([['1', '2', '3', '4'], ['5', '6', '7', '8'], ['9', 'a', 'b', 'c'], ['d', 'e', 'f', 'g']], [['d', '9', '5', '1'], ['e', 'a', '6', '2'], ['f', 'b', '7', '3'], ['g', 'c', '8', '4']]),
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
    ([[1, 2], [3, 4]], [[3, 1], [4, 2]])
]

for i, (x, y) in enumerate(tests):
    out = s.rotate(x)
    assert y == out, 'Test {}: Expect: {}, got {}'.format(i, y, out)

print('Example cases passed!')
