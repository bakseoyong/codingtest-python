from collections import deque

#메모리 128 메가


# z, y, x 순
moves = [[-1, 0, 0], [1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
queue = deque()

# E에 도달한다면 cnt값을 answer에 갱신하고, 그렇지 않다면 -1이 유지되니까 문자열 출력
answer = -1


def bfs(S, E):
    global answer

    visited = [[[False for x in range(C)] for y in range(R)] for z in range(L)]
    visited[S[0]][S[1]][S[2]] = True

    while queue:
        z, y, x, cnt = queue.popleft()

        for move in moves:
            if 0 <= z + move[0] < L and 0 <= y + move[1] < R and 0 <= x + move[2] < C \
                    and not visited[z + move[0]][y + move[1]][x + move[2]]:
                if building[z + move[0]][y + move[1]][x + move[2]] == '.':
                    queue.append((z+move[0], y+move[1], x+move[2], cnt + 1))
                    visited[z+move[0]][y+move[1]][x+move[2]] = True
                elif building[z + move[0]][y + move[1]][x + move[2]] == 'E':
                    answer = cnt + 1
                    visited.clear()
                    return
    visited.clear()


def solution():
    global answer
    answer = -1

    S = (0, 0, 0)
    E = (0, 0, 0)

    for z in range(L):
        for y in range(R):
            for x in range(C):
                if building[z][y][x] == 'S':
                    S = (z, y, x)
                elif building[z][y][x] == 'E':
                    E = (z, y, x)

    queue.append((S[0], S[1], S[2], 0))
    bfs(S, E)

    if answer != -1:
        print('Escaped in', answer , 'minute(s).')
    else:
        print('Trapped!')


if __name__ == '__main__':
    L, R, C = map(int, input().split())

    while not (L == 0 and R == 0 and C == 0):
        # 3차원 배열
        building = [[[] for _ in range(R)] for l in range(L)]

        # 동 서 남 북 상 하 이동 가능

        for l in range(L):
            for r in range(R):
                building[l][r] = input()
            input()  # 줄넘김 용으로 한 줄

        #print(building)

        solution()

        L, R, C = map(int, input().split())
        queue.clear()
        building.clear()
