import sys
import math

def non_recursive():
    for i in range(len(arrs)):
        dp[i][i] = 0

    for i in range(1, len(arrs)): #몇칸 간격으로 합을 구할 건지
        for j in range(0, len(arrs) - i): # 몇번 인덱스부터 시작할 건지
            for k in range(j, j + i): #몇칸 간격이면 중간을 갈라야 한다.
                dp[j][j + i] = min(dp[j][j + i], sums[j][k] + sums[k + 1][j + i] + dp[j][k] + dp[k + 1][j + i])

def recursive(start, end):
    # 종료 조건 (아래 if문에 포함됨)
    # if start == end:
    #     return dp[start][start]
    # 이미 이전에 탐색해서 최소값을 가지고 있는 상태라면
    if dp[start][end] != 10001:
        return dp[start][end]

    for i in range(start + 1, end + 1):
        if dp[start][i-1] == 10001:
            dp[start][i-1] = recursive(start, i-1)
        if dp[i][end] == 10001:
            dp[i][end] = recursive(i, end)

        # dp[start][end] = min(dp[start][end], dp[start][i - 1] + dp[i][end])

        if dp[start][end] > sums[start][i - 1] + sums[i][end] + dp[start][i-1] + dp[i][end]:
            dp[start][end] = sums[start][i - 1] + sums[i][end] + dp[start][i-1] + dp[i][end]

    return dp[start][end]

if __name__ =='__main__':
    T = int(input())

    for _ in range(T):
        a = int(input())

        arrs = list(map(int, sys.stdin.readline().split()))

        sums = [[0 for _ in range(len(arrs))] for _ in range(len(arrs))]
        dp = [[math.inf for _ in range(len(arrs))] for _ in range(len(arrs))]

        # print(sums)

        # sum arr
        # 본인걸 먼저 채우고, 그 다음은 부분 합으로 이전 sum 배열 + 지금 값 하면 되겠다.
        for i in range(len(arrs)):
            sums[i][i] = arrs[i]
            for j in range(i + 1, len(arrs)):
               sums[i][j] = sums[i][j - 1] + arrs[j]

        # print(sums)

        # dp arr 초기화

        start, end = 0, len(arrs) - 1
        # dp[start][end] = recursive(start, end)

        non_recursive()

        # print(dp)
        print(dp[start][end])