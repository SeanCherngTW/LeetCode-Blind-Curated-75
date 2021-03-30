class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.rows = len(board)
        self.cols = len(board[0])

        for i in range(self.rows):
            for j in range(self.cols):
                if board[i][j] == word[0] and self.backtrack(board, word, i, j):
                    return True
        return False

    def backtrack(self, board, word, i, j):
        if len(word) == 0:
            return True
        if i < 0 or i >= self.rows or j < 0 or j >= self.cols or word[0] != board[i][j]:
            return False

        board[i][j] = 1
        res = self.backtrack(board, word[1:], i - 1, j) or self.backtrack(board, word[1:], i + 1, j) or self.backtrack(board, word[1:], i, j - 1) or self.backtrack(board, word[1:], i, j + 1)

        board[i][j] = word[0]
        return res
