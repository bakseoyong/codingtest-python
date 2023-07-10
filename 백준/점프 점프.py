if __name__ == '__main__':
    N = int(input())

    arrs = list(map(int, input().split()))

    dp = [9999 for _ in range(N)]
    dp[0] = 0

    # print(arrs)
    for index in range(len(arrs)):
        for i in range(arrs[index]):
            search = index + i + 1
            if search >= N:
                search = N - 1
            dp[search] = min(dp[index] + 1, dp[search])

    if dp[N - 1] != 9999:
        print(dp[N-1])
    else:
        print(-1)

