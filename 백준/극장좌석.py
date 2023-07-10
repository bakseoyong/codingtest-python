if __name__ == '__main__':
    N = int(input())
    M = int(input())

    vips = []

    for _ in range(M):
        vips.append(int(input()))

    dp = [0 for _ in range(N + 1)]
    dp[0] = 1
    if N > 0:
        dp[1] = 1
    if N > 1:
        dp[2] = 2
    for i in range(3, N + 1):
        dp[i] = dp[i-1] + dp[i-2]

    answer = 1

    if not vips:
        answer = dp[N]
        print(answer)
    else:
        for i in range(len(vips)):
            if i == 0:
                answer *= dp[vips[i] - 1]
            else:
                answer *= dp[vips[i] - vips[i-1] - 1]

        answer *= dp[N - vips[len(vips) - 1]]
        print(answer)