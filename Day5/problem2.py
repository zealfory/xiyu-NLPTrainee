class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        s3_len = len(s3)
        
        # s1,s2长度之和与s3不符
        if s1_len + s2_len != s3_len:
            return False
        
        # 顺序拼接的情形
        if s1 + s2 == s3 or s2 + s1 == s3:
            return True
        
        # s3包含新字符的情形
        for s in s3:
            if (s1 + s2).find(s) == -1:
                return False
        
        # 动态矩阵
        length = s1_len if s1_len > s2_len else s2_len
        matrix = [[False for i in range(length + 1)] for i in range(length + 1)]
        #print(matrix)
        
        # 交错拼接的情形
        for i in range(s1_len + 1):
            for j in range(s2_len + 1):
                if i == 0 and j == 0:
                    matrix[i][j] = True
                elif i == 0:
                    # print(matrix[i][j-1])
                    # print(s2[j-1])
                    # print(s3[i+j-1])
                    matrix[i][j] = matrix[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                elif j == 0:
                    matrix[i][j] = matrix[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                else:
                    matrix[i][j] = (matrix[i][j - 1] and s2[j - 1] == s3[i + j - 1]) or \
                    (matrix[i - 1][j] and s1[i - 1] == s3[i + j - 1])
                
        return matrix[s1_len][s2_len]
