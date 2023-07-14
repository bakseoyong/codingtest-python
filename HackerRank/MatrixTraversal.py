def solve():
    n = int(input())
    m = int(input())

    arr = []
    dp = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        arr.append(list(map(int, input().split())))

    print(arr)

    dp[0][0] = arr[0][0]

    for i in range(n):
        for j in range(m):
            if i == 0:
                dp[i][j] = arr[i][j]
            else:
                if j == 0:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j+1]) + arr[i][j]
                elif j == m - 1:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + arr[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1]) + arr[i][j]

    print(dp)
    print(100 - min(dp[i][0:m]))


if __name__ == '__main__':
    solve()
