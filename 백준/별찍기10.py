
def print_star(col_front, col_end, row_front, row_end):
    col_mid = col_front + 1
    row_mid = row_front + 1

    for r in range(row_front, row_end):
        for c in range(col_front, col_end):
            if r == row_mid and c == col_mid:
                continue
            else:
                board[r][c] = '*'

# def print_blank(col_front, col_end, row_front, row_end):
#     for y in range(col_front, col_end):
#         for x  in range(row_front, row_end):
#             board[y][x]

def recursion(N, col_front, col_end, row_front, row_end):
    #이만큼 증가한다.
    increment = N // 3

    if increment == 1:
        print_star(col_front, col_end, row_front, row_end)
        return

    #1이 아니면 쪼개기
    for y in range(3):
        for x in range(3):
            if y == 1 and x == 1:
                # print_blank(increment * 1, increment * 2, increment *1, increment * 2)
                # '' 로 초기화 되어있으니 따로 update 안해줘도 된다.
                continue

            recursion(N // 3, col_front + increment * x, col_front + increment * (x + 1), row_front + increment * y, row_front + increment * (y + 1))


if __name__ == '__main__':
    N = int(input())

    board = [['' for a in range(N)] for b in range(N)]
    # print(board)

    recursion(N, 0, N, 0, N)


    for y in range(N):
        str = ''
        for x in range(N):
            if board[y][x] == '*':
                str += board[y][x]
            else:
                str += ' '
        print(str)
