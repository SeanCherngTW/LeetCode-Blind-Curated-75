class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        res = []
        rows = len(matrix)
        cols = len(matrix[0])

        row_start, row_end, col_start, col_end = 0, rows - 1, 0, cols - 1

        while row_start <= row_end and col_start <= col_end:

            # To Right
            for j in range(col_start, col_end + 1):
                res.append(matrix[row_start][j])
            row_start += 1

            # To Down
            for i in range(row_start, row_end + 1):
                res.append(matrix[i][col_end])
            col_end -= 1

            # To Left
            if row_start <= row_end:  # For n*m matrix that n < m
                for j in range(col_end, col_start - 1, -1):
                    res.append(matrix[row_end][j])
                row_end -= 1

            # To Up
            if col_start <= col_end:  # For n*m matrix that n > m
                for i in range(row_end, row_start - 1, -1):
                    res.append(matrix[i][col_start])
                col_start += 1

        return res
