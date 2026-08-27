class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        starts = []

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    starts.append((i,j))
        if not starts: return False

        def dfs(i, j, s, seen):
            s += board[i][j]
            seen.add((i, j))
            if len(s) == len(word):
                return word == s
            
            for dr, dc in dirs:
                nr, nc = i+dr, j+dc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in seen:
                    if dfs(nr, nc, s, seen.copy()):
                        return True
            return False
            

        for i, j in starts:
            if dfs(i, j, "", set()):
                return True

        return False