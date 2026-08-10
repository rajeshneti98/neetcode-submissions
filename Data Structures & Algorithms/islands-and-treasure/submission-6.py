class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = [[0] * cols for r in range(rows)]
        def isValid(r, c):
            return r>=0 and c>=0 and r<rows and c < cols and grid[r][c]!=-1 and not visited[r][c]
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited[r][c] = True
        while q:
            i, j = q.popleft()
            for dr, dc in directions:
                nr, nc = i+dr, j+dc
                if isValid(nr, nc):
                    visited[nr][nc] = True
                    grid[nr][nc] = min(grid[nr][nc], grid[i][j]+1)
                    q.append((nr, nc))
            

            

        