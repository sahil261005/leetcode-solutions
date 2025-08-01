class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(r, c, i):
            if i == len(word):
                return True  # All letters matched

            if (
                r < 0 or c < 0 or r >= ROWS or c >= COLS or
                word[i] != board[r][c] or (r, c) in visited
            ):
                return False

            visited.add((r, c))

            res = (
                dfs(r + 1, c, i + 1) or  # down
                dfs(r - 1, c, i + 1) or  # up
                dfs(r, c + 1, i + 1) or  # right
                dfs(r, c - 1, i + 1)     # left
            )

            visited.remove((r, c))  # backtrack
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        return False
