class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.rows = len(heights)
        self.cols = len(heights[0])
        for i in range(self.rows):
            for j in range(self.rows):
                self.path = []
                self.goal = [False, False]
                visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
                if i == 3 and j == 1:
                    self.dfs(heights, i, j, visited, 999)
                if self.goal == [True, True]:
                    return self.path
        return []

    def dfs(self, heights, i, j, visited, prev):
        if i >= self.rows or i < 0 or j >= self.cols or j < 0 or visited[i][j] or prev < heights[i][j]:
            return
        if i == 0 and j == self.cols - 1:
            self.goal[0] = True
            return
        if i == self.rows - 1 and j == 0:
            self.goal[1] = True
            return

        cur = heights[i][j]
        visited[i][j] = True
        self.path.append([i, j])

        self.dfs(heights, i + 1, j, visited, cur)
        self.dfs(heights, i - 1, j, visited, cur)
        self.dfs(heights, i, j + 1, visited, cur)
        self.dfs(heights, i, j - 1, visited, cur)

        visited[i][j] = False
        self.path.remove([i, j])
        return
