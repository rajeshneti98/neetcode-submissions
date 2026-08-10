class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        m , n = len(grid), len(grid[0])
        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]
        q1, q2 = deque(), deque()
        def isValid(x, y):
            return x>=0 and y>=0 and x< m and y<n
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for i in range(m):
            q1.append([i,0])
        for j in range(n):
            q1.append([0,j])
        for i in range(m):
            q2.append([i, n-1])
        for j in range(n):
            q2.append([m-1, j])
        while q1:
            size = len(q1)
            for i in range(size):
                x, y = q1.popleft()
                if not pacific[x][y]:
                    pacific[x][y] = True
                    for dx, dy in directions:
                        x1, y1 = x+ dx, y+ dy
                        if isValid(x1, y1) and  not pacific[x1][y1] and grid[x1][y1] >= grid[x][y]:
                            q1.append([x1,y1])
        while q2:
            size = len(q2)
            for i in range(size):
                x, y = q2.popleft()
                if not atlantic[x][y]:
                    atlantic[x][y] = True
                    for dx, dy in directions:
                        x1, y1 = x + dx, y + dy
                        if isValid(x1, y1) and not atlantic[x1][y1] and grid[x1][y1] >= grid[x][y]:
                            q2.append([x1,y1])
        res = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i,j])
        return res
        