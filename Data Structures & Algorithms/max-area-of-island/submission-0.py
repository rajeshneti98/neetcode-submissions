class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def isValid(i,j):
            return i>=0 and j>=0 and i<m and j<n and grid[i][j] == 1 
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
        def dfs(i,j):
            grid[i][j] = 0
            res = 1
            for [x, y] in directions:
                if isValid(i+x, j+y):
                    res+=dfs(i+x, j+y)
            return res
        maxArea = 0
        for i in range(m):
            for j in range(n):
                if isValid(i,j):
                    maxArea = max(maxArea, dfs(i, j))
        return maxArea
                    


            
            
        