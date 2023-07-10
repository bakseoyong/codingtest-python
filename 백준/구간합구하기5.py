if __name__ == '__main__':
    N, M = map(int, input().split())

    board = [[0 for _ in range(N)] for _ in range(N)]
    test = [[0 for _ in range(4)] for _ in range(M)]
    dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

    for i in range(N):
        board[i] = list(map(int, input().split()))

    for i in range(M):
        test[i] = list(map(int, input().split()))
    # print(board)
    # print(test)

    # sum
    for y in range(1, N + 1):
        for x in range(1, N + 1):
            if y == 1 and x == 1:
                dp[y][x] = board[0][0]
                continue
            if y == 1:
                dp[1][x] = dp[1][x-1] + board[0][x-1]
            elif x == 1:
                dp[y][1] = dp[y-1][1] + board[y-1][0]
            else:
                dp[y][x] = dp[y-1][x] + dp[y][x-1] + board[y-1][x-1] - dp[y-1][x-1]

    # print(dp)

    for t in test:
        y1, x1, y2, x2 = t

        print(dp[y2][x2] - dp[y2][x1 - 1] - dp[y1 - 1][x2] + dp[y1 -1][x1 - 1])

