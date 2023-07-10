import math

def solve():
    num = int(input())

    tournament = list(map(int, input().split()))

    sum = [[math.inf for _ in range(num)] for _ in range(num)]
    winner = [[0 for _ in range(num)] for _ in range(num)]

    for i in range(num):
        winner[i][i] = tournament[i]
        sum[i][i] = 0

    #bottom-up
    for i in range(1, num): #범위(2칸부터)
        for j in range(num - i): #시작인덱스
            for k in range(j, j + i): #탐색 경계
                #값 계산
                #winner는 min값이 갱신될때 변경
                diff = int(math.fabs(winner[j][k] - winner[k+1][j+i]))
                if sum[j][j + i] > sum[j][k] + sum[k+1][j+i] + diff:
                    sum[j][j + i] = sum[j][k] + sum[k+1][j+i] + diff
                    winner[j][j+i] = min(winner[j][k], winner[k+1][j+i])

    print(sum[0][num - 1])


if __name__ == '__main__':
    solve()