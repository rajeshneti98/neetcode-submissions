class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def isValid(i, j):
            return i>=0 and j>=0 and i<m and j<n  and grid[i][j] == '1'
        dir = [[0,1], [0, -1], [1, 0], [-1, 0]]
        def dfs(i,j):
            if grid[i][j]!='1':
                return
            grid[i][j] = '0'
            for [x,y] in dir:
                if isValid(i+x, j+y):
                    dfs(i+x, j+y)
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count+=1
                    dfs(i,j)
        return count
        
        