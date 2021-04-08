class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return []
        if not matrix[0]:
            return [[]]

        rows = len(matrix)
        cols = len(matrix[0])

        zero_rows = set()
        zero_cols = set()

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        for i in zero_rows:
            for j in range(cols):
                matrix[i][j] = 0

        for j in zero_cols:
            for i in range(rows):
                matrix[i][j] = 0

    def setZeroesV2(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return []
        if not matrix[0]:
            return [[]]

        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    for _i in range(rows):
                        matrix[_i][j] = 0
                    for _j in range(cols):
                        matrix[i][_j] = 0
