# 59퍼 틀렸습니다.

if __name__ == '__main__':
    T = int(input())

    dp = [0 for _ in range(10000)]

    dp[0] = 1
    dp[1] = 2
    dp[2] = 4
    for i in range(3, 10000):
        dp[i] = 1 + (i + 1) // 2
        for j in range((i + 1) // 3):
            dp[i] += ((i + 1) - 3 * (j + 1)) // 2 + 1


    for _ in range(T):
        a = int(input())

        print(dp[a - 1])

