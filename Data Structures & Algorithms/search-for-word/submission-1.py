class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(i, j, idx, seen):
            if not 0 <= i < m or not 0 <= j < n: return False
            if (i,j) in seen: return False
            if board[i][j] != word[idx]: return False
            if idx == len(word)-1: return True

            seen.add((i, j))
            for di, dj in dirs:
                if dfs(i+di, j+dj, idx+1, seen.copy()):
                    return True
            return False


        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0, set()):
                        return True
        return False