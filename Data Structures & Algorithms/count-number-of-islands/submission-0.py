class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    self.dfs(grid, r, c)
        return islands 

    def dfs(self, grid, r, c):
        if r < 0 or r >= len(grid):
            return 

        if c < 0 or c >= len(grid[0]):
            return 

        if grid[r][c] != '1':
            return 

        grid[r][c] = '#'
        self.dfs(grid, r + 1, c)
        self.dfs(grid, r - 1, c)
        self.dfs(grid, r, c + 1)
        self.dfs(grid, r, c - 1)

