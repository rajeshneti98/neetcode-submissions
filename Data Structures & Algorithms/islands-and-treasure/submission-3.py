class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        rows = len(grid)
        cols = len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def isValid(r, c):
            return r>=0 and c>=0 and r<rows and c < cols and grid[r][c]!=-1
        def bfs(r, c):
            visited = [[0] * cols for r in range(rows)]
            q = deque()
            visited[r][c] = True
            q.append((r, c))
            while q:
                i, j = q.popleft()
                for dr, dc in directions:
                    nr, nc = i+dr, j+dc
                    if isValid(nr, nc) and not visited[nr][nc]:
                        visited[nr][nc] = True
                        grid[nr][nc] = min(grid[nr][nc], grid[i][j]+1)
                        q.append((nr, nc))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    bfs(r, c)
            

            

        