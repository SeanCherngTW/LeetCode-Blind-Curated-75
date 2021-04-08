class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board:
            return []

        res = []
        rows = len(board)
        cols = len(board[0])

        for word in words:
            for i in range(rows):
                for j in range(cols):
                    if board[i][j] == word[0] and self.hasWord(board, i, j, rows, cols, word):
                        if word not in res:
                            res.append(word)
                            break
        return res

    def hasWord(self, board, i, j, rows, cols, word):
        if len(word) == 0:
            return True
        if i < 0 or j < 0 or i >= rows or j >= cols or board[i][j] != word[0]:
            return False

        board[i][j] = '.'  # visited

        res = self.hasWord(board, i + 1, j, rows, cols, word[1:]) or self.hasWord(board, i - 1, j, rows, cols, word[1:]) or self.hasWord(board, i, j + 1, rows, cols, word[1:]) or self.hasWord(board, i, j - 1, rows, cols, word[1:])

        board[i][j] = word[0]

        return res
