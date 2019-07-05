class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        t_len = len(t)
        s_len = len(s)
        # 动态矩阵
        matrix = [[0 for i in range(s_len + 1)] for i in range(t_len + 1)]

        for j in range(s_len + 1):
            matrix[0][j] = 1

        for i in range(1, t_len + 1):
            for j in range(1, s_len + 1):
                if t[i - 1] == s[j - 1]:
                    matrix[i][j] = matrix[i - 1][j - 1]  + matrix[i][j - 1]
                    #print(matrix)
                else:
                    matrix[i][j] = matrix[i][j - 1]
                
        return matrix[t_len][s_len]
