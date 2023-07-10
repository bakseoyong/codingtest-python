dp = []

def recursive(i, j):
    global dp

    if dp[i][j] != 0:
        return dp[i][j]
    else:
        sum = 0
        for k in range(i + 1):
            now = i - k
            sum += recursive(now, j - 1)
        dp[i][j] = sum
        return dp[i][j]

def solution(N, K):
    global dp

    dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

    for i in range(0, N + 1):
        dp[i][1] = 1

    for i in range(0, N + 1):
        for j in range(0, K + 1):
            dp[i][j] = recursive(i, j)

    print(dp[N][K] % 1000000000)

if __name__ == '__main__':
    N, K = map(int, input().split())

    solution(N, K)
