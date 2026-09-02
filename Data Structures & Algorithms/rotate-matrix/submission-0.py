class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)//2):
            tmp = matrix[i]
            matrix[i] = matrix[len(matrix)-i-1]
            matrix[len(matrix)-i-1] = tmp
        
        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp