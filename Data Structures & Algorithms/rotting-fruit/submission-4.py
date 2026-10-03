class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        num_fresh = 0
        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    num_fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
        res = 0
        while q and num_fresh:

            for _ in range(len(q)):
                x, y = q.popleft()
                
                for dx, dy in dirs:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < m and 0 <= ny < n:
                        if grid[nx][ny] == 1:
                            grid[nx][ny] = 2
                            num_fresh -= 1
                            q.append((nx, ny))
            res += 1
        
        return -1 if num_fresh > 0 else res