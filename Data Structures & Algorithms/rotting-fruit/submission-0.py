class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        seen = [[False for _ in range(n)] for _ in range(m)]

        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append([i,j])

        level = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for i, j in dirs:
                    nr = r + i
                    nc = c + j
                    if nr < 0 or nr >= m or nc < 0 or nc >= n: continue
                    if seen[nr][nc] or grid[nr][nc] != 1: continue
                    seen[nr][nc] = True
                    grid[nr][nc] = 2
                    q.append([nr, nc])
            
            if q: level += 1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: return -1
        return level