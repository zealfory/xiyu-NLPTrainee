import math
class Solution:
    def myAtoi(self, str: str) -> int:
        flag = 1 # 正负号
        str = str.strip()
        max_value = int(math.pow(2, 31) - 1)
        min_value = int(-math.pow(2, 31))
        if len(str) == 0:
            return 0
        if str.isdigit():
            res = int(str)

        if str[0] == '-' or str[0] == '+':
            if str[0] == '-':
                flag = -1
            str = str[1:]
            
        if len(str) != 0 and str[0].isdigit():
            s = ""       
            for i in str:
                if i.isdigit():
                    s += i
                else:
                    break
            if len(s) != 0:
                res = int(s) * flag
        else:
            return 0

        if res > max_value:
            return max_value
        elif res < min_value:
            return min_value
        else:
            return res
        