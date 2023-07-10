def solution():
    for _ in range(N):
        if _ + T[_] < N:
            if dp[_ + T[_]][0] < dp[_][0] + P[_]:
                for i in range(_ + T[_], N):
                    dp[i][0] = max(dp[_][0] + P[_], dp[i][0])
        if _ + T[_] - 1 < N:
            if dp[_ + T[_] - 1][1] < dp[_][0] + P[_]:
                for i in range(_ + T[_] - 1, N):
                    dp[i][1] = max(dp[_][0] + P[_], dp[i][1])

    print(max(dp[N - 1][0], dp[N - 1][1]))

if __name__ == '__main__':
    N = int(input())

    dp = [[0 for i in range(2)] for _ in range(N)]

    T = [0 for _ in range(N)]
    P = [0 for _ in range(N)]

    for _ in range(N):
        T[_], P[_] = map(int, input().split())

    # print(T)
    # print(P)
    solution()
