def dfs(y, x):
    global arr, discover, finished, cycle

    if not discover[y][x]:
        discover[y][x] = True
        if arr[y][x] == 'U':
            dfs(y-1, x)
        elif arr[y][x] == 'D':
            dfs(y+1, x)
        elif arr[y][x] == 'L':
            dfs(y, x-1)
        elif arr[y][x] == 'R':
            dfs(y, x+1)
    else:
        if not finished[y][x]:
            cycle += 1

    finished[y][x] = True


def solve():
    global arr, discover, finished, cycle

    cycle = 0
    n, m = map(int, input().split())

    arr = []
    discover = [[False for _ in range(m)] for _ in range(n)]
    finished = [[False for _ in range(m)] for _ in range(n)]

    for i in range(n):
        arr.append(input())

    for i in range(n):
        for j in range(m):
            if not discover[i][j]:
                dfs(i, j)
    print(cycle)


if __name__ == '__main__':
    solve()