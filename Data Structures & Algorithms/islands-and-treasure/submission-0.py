class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        q = deque()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append([i,j])
        visited = set()
        def isValid(x, y):
            return x>=0 and y>=0 and x<m and y<n and grid[x][y]!=-1 and (x,y) not in visited
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q:
            size = len(q)
            print(q)
            for i in range(size):
                curr = q.popleft()
                visited.add((curr[0], curr[1]))
                for [dx, dy] in dirs:
                    x, y = curr[0]+ dx, curr[1]+ dy
                    if isValid(x, y):
                        grid[x][y] = min(grid[x][y], 1+ grid[curr[0]][curr[1]])
                        q.append([x, y])
        