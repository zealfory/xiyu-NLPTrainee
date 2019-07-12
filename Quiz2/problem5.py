class Solution:
    def convert(self, s: str, numRows: int) -> str:
        matrix_s = [''] * numRows
        i = 0
        while i < len(s):
            for j in range(numRows):
                if i < len(s):
                    matrix_s[j] += s[i]
                    i += 1
            for k in range(numRows - 2, 0, -1):
                if i < len(s):
                    matrix_s[k] += s[i]
                    i += 1
        return ''.join(matrix_s)