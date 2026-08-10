class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        m , n = len(grid), len(grid[0])
        freshCount = 0

        def isValid(x, y):
            return x>=0 and y>=0 and x<m and y<n and grid[x][y]==1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append([i,j])
                    grid[i][j] = 3
                elif grid[i][j] == 1:
                    freshCount += 1
        if freshCount == 0:
            return 0
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        count = 0
        while q:
            size = len(q)
            count+= 1
            for i in range(size):
                curr = q.popleft()
                for [dx, dy] in dirs:
                    x, y = curr[0]+ dx, curr[1] + dy
                    if isValid(x, y):
                        grid[x][y] = 3
                        q.append([x,y])
                        freshCount-=1
            if freshCount<=0:
                break
        return count if freshCount == 0 else -1

        