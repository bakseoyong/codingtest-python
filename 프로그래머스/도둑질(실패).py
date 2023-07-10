
def solution(money):
    answer = 0

    #dynamic programing
    # 0이상 1000이하니까 무조건 털면 이득이다.
    # dp[1] = 1번집 털기 1
    # dp[2] = 1번집 털기 (dp[1]) or 2번집 1000
    # dp[3] = dp[1] + 3번집 탈기, dp[2] 1000
    # dp[4] = dp[2] + 4번집 털기, dp[3] 1003
    #
    # 1 1000 2 3 4000 5 1000


    # 1 1000 2000 5000 7000

    dp = [0 for i in range(len(money) + 1)]

    dp[1] = money[1 - 1]
    dp[2] = max(dp[1], money[2 - 1])
    for index in range(3, len(dp)):
        #print(index)
        dp[index] = max(dp[index - 2] + money[index - 1], dp[index - 1])

    print(dp[len(money)])

    answer = dp[len(money)]
    return answer

if __name__ == '__main__':
    money = [1, 1000, 2000, 9000, 6000]
    solution(money)
