class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        seen = [[False for _ in range(n)] for _ in range(m)]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        x, y = 0, 0
        res = []

        d = 0
        for _ in range(m*n):
            seen[x][y] = True
            res.append(matrix[x][y])
            nx, ny = (dirs[d][0]+x, dirs[d][1]+y)

            if not 0 <= nx < m or not 0 <= ny < n or seen[nx][ny]:
                d = (d+1) % 4
                x, y = (dirs[d][0]+x, dirs[d][1]+y)
            else:
                x, y = nx, ny
        
        return res