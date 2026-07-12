class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        chunks = board.copy()
        
        for i in range(9):
            col = []
            for j in range(9):
                col.append(board[j][i])
            chunks.append(col)


        for i in range(3):
            for j in range(3):
                chunk = []
                for ii in range(3):
                    for jj in range(3):
                        chunk.append(board[jj+3*j][ii+3*i])
                chunks.append(chunk)
                print(chunk)

        for c in chunks:
            if self.isValidChunk(c):
                continue
            else:
                return False
        return True

        
    def isValidChunk(self, chunk: List[str]) -> bool:
        nums = []
        for x in chunk:
            if x.isnumeric():
                nums.append(x)
        return len(nums) == len(set(nums))