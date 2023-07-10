from collections import deque
max_v = 0
moves = [[-1, 0], [1,0], [0, -1], [0, 1]]
queue = deque()
n = 0
m = 0
maps = []

# 이 둘 사이의 최단거리의 최댓값..
# 52% 반례 - 1 2 LL => 2 x 정답 1
# 57% 이후 시간초과

def bfs(i, j):
    global max_v

    visited = [[False for _ in range(m)] for k in range(n)]
    visited[i][j] = True

    while len(queue) > 0:
        y, x, cnt = queue.popleft()

        max_v = max(cnt, max_v)

        for move in moves:
            if 0 <= y + move[0] < n and 0 <= x + move[1] < m:
                if maps[y + move[0]][x + move[1]] == 'L' and not visited[y + move[0]][x + move[1]]:
                    visited[y + move[0]][x + move[1]] = True
                    queue.append((y + move[0], x + move[1], cnt + 1))


def solution():
    global queue, max_v, n, m, maps

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'L':
                queue.append((i, j, 0))
                bfs(i, j)


if __name__ == '__main__':

    n, m = map(int, input().split())

    maps = [[] for _ in range(n)]

    for i in range(n):
        maps[i] = input()

    # print(maps)
    solution()

    print(max_v)