import math

def solution(alp, cop, problems):
    answer = 0

    dp = [[math.inf for _ in range(151)] for _ in range(151)]

    for i in range(0, alp + 1):
        for j in range(0, cop + 1):
            dp[i][j] = 0

    for i in range(alp, 151):
        for j in range(cop, 151):
            if i == alp and j == cop:
                continue

            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1)
            for problem in problems:
                if (i - problem[2]) >= problem[0] and (j - problem[3]) >= problem[1]:
                    dp[i][j] = min(dp[i - problem[2]][j - problem[3]] + problem[4], dp[i][j])

    # for i in range(10, 20):
    #     for j in range(10, 20):
    #         print('i, j : ', i, j, 'time is : ', dp[i][j])

    for problem in problems:
        answer = max(answer, dp[problem[0]][problem[1]])

    print(answer)
    return answer

if __name__ == '__main__':
    alp = 0
    cop = 0
    problems = [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]

    solution(alp, cop, problems)







    #
    # [10][10] = 0
    # [10][11] = max(dp[10][10] + 1, dp[9][11] + 1)
    # [10][12] = dp[10][11] + 1
    # [12][10] = dp[11][10] + 1
    # [12][16] = dp[10][15] + problems.cost, dp[12][14] + 1, dp[11][15] + 1)
    #
    # 반대로 한다면?
    # 20, 20에서 10, 10까지 간다고 생각한다면?
    # -> 어렵다. 가장 어려운문제가 한개라고 정해진게 아니라서
    #
    #
