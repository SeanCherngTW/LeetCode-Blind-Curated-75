class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        res = 0
        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    self.walkIsland(grid, i, j, rows, cols)
                    res += 1

        return res

    def walkIsland(self, grid, i, j, rows, cols):
        if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] != '1':
            return
        grid[i][j] = '-1'
        self.walkIsland(grid, i + 1, j, rows, cols)
        self.walkIsland(grid, i - 1, j, rows, cols)
        self.walkIsland(grid, i, j + 1, rows, cols)
        self.walkIsland(grid, i, j - 1, rows, cols)
