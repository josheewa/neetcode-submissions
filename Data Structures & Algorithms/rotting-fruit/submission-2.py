class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()
        fresh = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2: q.append((r, c))
                elif grid[r][c] == 1: fresh += 1
        
        mins = 0
        while q and fresh:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in dirs:
                    nr = r + dr
                    nc = c + dc
                    if (0 <= nr < len(grid) 
                    and 0 <= nc < len(grid[0])
                    and grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
            if q: mins += 1
        return mins if fresh == 0 else -1