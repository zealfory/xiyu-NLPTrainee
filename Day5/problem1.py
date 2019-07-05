class Solution:
    def minCut(self, s: str) -> int:
        s_len = len(s)
        # 动态list
        cut_result = [i for i in range(s_len + 1)]
        # 长度<=1, 不能分割
        if s_len <= 1:
            return 0
        
        for i in range(1, s_len + 1):
            for j in range(i):
                cut_s = s[j: i]
                if cut_s == cut_s[::-1]:
                    cut_result[i] = min(cut_result[j] + 1, cut_result[i])
        return cut_result[s_len] - 1
                
