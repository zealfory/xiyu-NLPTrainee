from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = len(s) + 1
        index_l, index_r, true_l, true_r = 0, 0, 0, 0
        already = 0
        dict_t = Counter(t)
        dict_sub = {}
        while index_r < len(s):
            c = s[index_r]
            if c in dict_sub:
                dict_sub[c] += 1
            else:
                dict_sub[c] = 1
            if c in t and dict_sub[c] == dict_t[c]:
                already += 1
            while index_l <= index_r and already == len(dict_t):
                char = s[index_l]
                curr_ans = index_r - index_l + 1
                if curr_ans < ans:
                    ans = curr_ans
                    true_l = index_l
                    true_r = index_r
                dict_sub[char] -= 1
                if char in dict_t and dict_sub[char] < dict_t[char]:
                    already -= 1
                index_l += 1
            index_r +=1
                
        if ans == len(s) + 1:
            return ""
        else:
            return s[true_l: true_r + 1]
                
            
         
        