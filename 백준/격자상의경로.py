def solution(n, m, o):
    dp = [[1 for _ in range(m)] for _ in range(n)]
    #print(dp)

    #o가 0일떄 따로 조건을 설정해 주지 않아도 되겠다. 0을 여기에 넣으면 (0, 0)이 나올 것이고
    #그게 어차피 시작점이기 때문에 1 * 도착점 까지가 되어서 값이 구해진다.
    o_r, o_c = o // n - 1, o % m - 1
    if o_r == -1 and o_c == -1:
        o_r, o_c = 0, 0


    #시작점부터 동그라미까지
    for y in range(0, o_r + 1):
        for x in range(0, o_c + 1):
            if y == 0 or x == 0:
                continue
            else:
                dp[y][x] = dp[y-1][x] + dp[y][x-1]

    middle = dp[o_r][o_c]
    dp[o_r][o_c] = 1

    #동그라미부터 마지막까지
    for y in range(o_r, n):
        for x in range(o_c, m):
            if y == o_r or x == o_c:
                continue
            else:
                dp[y][x] = dp[y-1][x] + dp[y][x-1]

    print(dp[n - 1][m - 1] * middle)


if __name__ == '__main__':
    n, m, o = map(int, input().split())

    solution(n, m, o)