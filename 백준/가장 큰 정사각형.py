

def solve():
    answer = 0
    n, m = map(int, input().split())

    board = []

    for i in range(n):
        board.append(input())

    #i -1, j -1 좌표가 정사각형임이 확인되면, 나의 정사각형이 꽉 차있음을 보증
    square = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    #첫 행, 열 탐색때 수월하게 하기위해 + 1
    row_dp = [[ 0 for _ in range(m + 1)] for _ in range(n + 1)]
    col_dp = [[ 0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if board[i - 1][j - 1] == '1':
                #row, col은 + 1 에 맞게
                #길이 갱신
                row_dp[i][j] = row_dp[i][j-1] + 1
                col_dp[i][j] = col_dp[i-1][j] + 1


                rec_len = min(row_dp[i][j], col_dp[i][j])
                if rec_len == 1:
                    square[i][j] = 1
                    answer = max(answer, 1)

                else:
                    square[i][j] = int((square[i - 1][j - 1] ** (1/2) + 1) ** 2)
                    square[i][j] = min(square[i][j], rec_len * rec_len)
                    answer = max(answer, square[i][j])


    print(answer)



if __name__ == '__main__':
    solve()