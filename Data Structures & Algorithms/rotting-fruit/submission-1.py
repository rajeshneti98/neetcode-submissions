class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshOranges = 0
        time = 0
        rows, cols = len(grid), len(grid[0])
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    freshOranges+=1
                elif grid[r][c] == 2:
                    q.append((r, c))
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def isValid(r, c):
            return r>=0 and r<rows and c>=0 and c<cols and grid[r][c] == 1
        while freshOranges > 0 and len(q)>0:
            time+=1
            n = len(q)
            for i in range(n):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if isValid(nr, nc):
                        freshOranges-=1
                        grid[nr][nc] = 2
                        q.append((nr, nc))
        if freshOranges == 0:
            return time
        return -1