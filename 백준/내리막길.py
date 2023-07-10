import sys
sys.setrecursionlimit(10 ** 6)

def dfs(y, x):
    dp[y][x] = 0

    for move in moves:
        if 0 <= y + move[0] < N and 0 <= x + move[1] < M:
            if maps[y + move[0]][x + move[1]] > maps[y][x]:
                if dp[y + move[0]][x + move[1]] == -1:
                    dp[y][x] += dfs(y + move[0], x + move[1])
                else:
                    dp[y][x] += dp[y + move[0]][x + move[1]]

    return dp[y][x]

if __name__ == '__main__':
    N, M = map(int, input().split())

    dp = [[-1 for _ in range(M)] for _ in range(N)]
    dp[0][0] = 1
    #print(dp)
    maps = [[] for _ in range(N)]

    for _ in range(N):
        maps[_] = list(map(int, input().split()))

    moves = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    dfs(N-1, M-1)

    print(dp[N-1][M-1])
