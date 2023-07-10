board = []
dp = []
N = 0

def recursive(y, x):
    #print(y, x)
    if dp[y][x] != 0:
        return dp[y][x]
    else:
        for i in range(0, y):
            if board[i][x] + i == y:
                #맞는 길
                dp[y][x] += recursive(i, x)

        for i in range(0, x):
            if board[y][i] + i == x:
                dp[y][x] += recursive(y, i)

        return dp[y][x]

if __name__ == '__main__':
    N = int(input())

    board = [[] for _ in range(N)]
    dp = [[0 for _ in range(N)] for _ in range(N)]
    dp[0][0] = 1

    for i in range(N):
        board[i] = list(map(int, input().split()))

    #print(board)
    recursive(N-1, N-1)

    print(dp[N-1][N-1])