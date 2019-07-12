class Solution:
    def calculate(self, s: str) -> int:
        ans = 0
        operators = []
        flag = [1]
        operator = ""
        for char in s:
            if char == " ":
                continue
            elif char == "+" and operator != "":
                flag.append(1)
                operators.append(operator)
                operator = ""
            elif char == "-" and operator != "":
                flag.append(-1)
                operators.append(operator)
                operator = ""
            else:
                operator += char
                
        operators.append(operator)
        for i, o in enumerate(operators):
            ans += flag[i] * self.product_div(o)
            #print(ans)
        return ans
    
    def product_div(self, s):
        """ 计算乘除法部分 """
        ans = 1
        operator = ""
        last = "*"
        for i, char in enumerate(s):
            if char == "*" or char == "/" or i == len(s) -1:
                if i != len(s) -1:
                    num = int(operator)
                else:
                    num = int(operator + char)
                if last == "*":
                    ans *= num
                    last = char
                    operator = ""
                elif last == "/":
                    ans //= num
                    last = char
                    operator = ""
            else:
                operator += char
        return ans
                    
                    