def divide(N, col_front, col_end, row_front, row_end):
    global answer

    col_mid = (col_front + col_end) // 2
    row_mid = (col_front + col_end) // 2

    #종료 조건
    if N == 1:
        answer += 1
        return

    #2사분면
    if col_front <= c < col_mid and row_front <= r < row_mid:
        answer += 0
        col_end = col_mid
        row_end = row_mid
        divide(N // 2, col_front, col_end, row_front, row_end)
        return

    #1사분면
    if col_mid <= c < col_end and row_front <= r < row_mid:
        answer += (N // 2) ** 2
        col_front = col_mid
        row_end = row_mid
        divide(N // 2, col_front, col_end, row_front, row_end)
        return

    #3사분면
    if col_front <= c < col_mid and row_mid <= r < row_end:
        answer += ((N // 2) ** 2) * 2
        col_end = col_mid
        row_front = row_mid
        divide(N // 2, col_front, col_end, row_front, row_end)
        return

    #4사분면
    if col_mid <= c < col_end and row_mid <= r < row_end:
        answer += ((N // 2) ** 2) * 3
        col_front = col_mid
        row_front = row_mid
        divide(N // 2, col_front, col_end, row_front, row_end)
        return

def solution(N, r, c):
    divide(2**N, 0, 2**N, 0, 2**N)

    print(answer)


if __name__ == '__main__':
    answer = -1;
    N, r, c = map(int, input().split())

    solution(N, r, c)