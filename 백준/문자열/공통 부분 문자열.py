def solve():
    str1 = input()
    str2 = input()

    dp = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
    answer = 0
    for i in range(len(str2)):
        if str1[0] == str2[i]:
            dp[0][i] = 1
    for i in range(len(str1)):
        if str2[0] == str1[i]:
            dp[i][0] = 1

    for i in range(1, len(str1)):
        for j in range(1, len(str2)):
            if str1[i] == str2[j]:
                dp[i][j] = dp[i-1][j-1] + 1
                answer = max(answer, dp[i][j])

    print(answer)

if __name__ == '__main__':
    solve()