def isValid(s):
    """
    :para s: str -- 字符串
    :return: bool -- 判定结果
    """
    # 栈
    stack = []

    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
 
        if char in mapping:
            # 开括号出栈或#
            top_element = stack.pop() if stack else '#'
            # 栈顶不匹配
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    # 栈空则判定有效
    return not stack


# test
def main():
    print(isValid("()"))
    print(isValid("()[]{}"))
    print(isValid("(]"))
    print(isValid("([)]"))
    print(isValid("{[]}"))

if __name__ == "__main__":
    main()