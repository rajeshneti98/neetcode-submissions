class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        rows = len(grid)
        cols = len(grid[0])
        def isValid(r, c):
            return r >= 0 and r< rows and c>=0 and c<cols and grid[r][c] == 1
        def dfs(r, c):
            grid[r][c] = 0
            area = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if isValid(nr, nc):
                    area  += dfs(nr, nc)
            return area
        maxArea = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r, c))
        return maxArea


