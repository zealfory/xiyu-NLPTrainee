def longestValidParentheses(s):
        """
        :para s: str -- 字符串
        :return: int -- 最长有效括号串长度
        """
        s_length = len(s)
        stack = []
        start = 0
        maxlen = 0
        for i in range(s_length):
            # 左括号入栈
            if s[i] == '(':
                stack.append(i)
            
            # 右括号
            else:
                # 栈空则更改起始点
                if len(stack) == 0:
                    start = i + 1
                    continue
                # 栈非空则出栈
                else:
                    a = stack.pop()
                    
                    # 更新最大长度值
                    if len(stack) == 0:
                        maxlen = max(i - start + 1, maxlen)
                    
                    else:
                        maxlen = max(i-stack[-1], maxlen)
 
        return maxlen

# test
def main():
    print(longestValidParentheses("(()"))
    print(longestValidParentheses(")()())"))

if __name__ == "__main__":
    main()