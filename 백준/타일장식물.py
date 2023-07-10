
def solution(n):
    dp = [0 for _ in range(n + 1)]

    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    #둘레 구하기
    answer = dp[n] * 2 + dp[n - 1] * 2
    print(answer)

if __name__ == '__main__':
    n = int(input())

    solution(n)