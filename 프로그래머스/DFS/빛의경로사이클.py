num = None
finished = None
moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
answer = None
grid = None
n = 0
m = 0


def dfs(y, x, move_index, tracking_num, grid):
    global num, finished, answer, moves, n, m

    if num[y][x][move_index] == 0:
        num[y][x][move_index] = tracking_num + 1

        if grid[y][x] == 'S':
            dfs((y + moves[move_index][0]) % n, (x + moves[move_index][1]) % m, move_index, tracking_num + 1, grid)
        elif grid[y][x] == 'L':
            dfs((y + moves[(move_index - 1) % 4][0]) % n, (x + moves[(move_index - 1) % 4][1]) % m, (move_index - 1) % 4, tracking_num + 1, grid)
        elif grid[y][x] == 'R':
            dfs((y + moves[(move_index + 1) % 4][0]) % n, (x + moves[(move_index + 1) % 4][1]) % m, (move_index + 1) % 4, tracking_num + 1, grid)
    else:
        if not finished[y][x][move_index]:
            # 첫번쨰, 두번쨰 탐색이 둘 다 1이기 때문에(if조건이 0이라서 맨 첫 탐색도 1을 줄 수 밖에 없었다.) 1 더해줘야 한다.
            answer.append(tracking_num - num[y][x][move_index] + 1)
    finished[y][x][move_index] = True


def solution(grid):
    global num, finished, answer, n, m
    n, m = len(grid), len(grid[0])
    answer = []

    num = [[[0 for _ in range(4)] for _ in range(m)] for _ in range(n)]
    finished = [[[False for _ in range(4)] for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            for k in range(4):
                dfs(i, j, k, 0, grid)
    answer.sort()

    return answer

if __name__ == '__main__':
    solution(["S"])
    solution(["R","R"])