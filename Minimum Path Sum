class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dp = [[float("inf")] * (COLS + 1) for _ in range(ROWS + 1)]
        dp[ROWS - 1][COLS] = 0

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                dp[r][c] = grid[r][c] + min(dp[r + 1][c], dp[r][c + 1])

        return dp[0][0]
