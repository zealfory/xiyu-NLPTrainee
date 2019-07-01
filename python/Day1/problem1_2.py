def generateParenthesis(N):
    """
    :para N: int -- 括号对数
    :return: list -- 有效括号组合
    """
    ans = []
    def b_track(S = '', left = 0, right = 0):
        # 已有N对括号
        if len(S) == 2 * N:
            ans.append(S)
            return
        # 左括号数少于N
        if left < N:
            b_track(S+'(', left+1, right)
        # 右括号数少于左括号数
        if right < left:
            b_track(S+')', left, right+1)

    b_track()
    return ans

# test
def main():
    print(generateParenthesis(3))


if __name__ == "__main__":
    main()