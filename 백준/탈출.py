from collections import deque

moves = [[-1, 0], [1, 0], [0, 1], [0, -1]]
water_queue = deque()
beaver_queue = deque()

def solution():
    print(1)

if __name__ == '__main__':
    answer = -1

    R, C = map(int, input().split())

    maps = [[] for _ in range(R)]

    for i in range(R):
        maps[i] = input()

    waters = []
    stones = []
    S = (0, 0)
    D = (0, 0)

    for i in range(R):
        for j in range(C):
            if maps[i][j] == 'S':
                S = (i, j)
            elif maps[i][j] == 'D':
                D = (i, j)
            elif maps[i][j] == '*':
                waters.append((i, j))
            elif maps[i][j] == 'X':
                stones.append((i, j))

    floor_timeline = [[-1 for _ in range(C)] for i in range(R)]
    #굴 위치
    floor_timeline[D[0]][D[1]] = 99999

    #돌 위치
    for stone in stones:
        floor_timeline[stone[0]][stone[1]] = 0

    #물 위치
    for water in waters:
        floor_timeline[water[0]][water[1]] = 0
        water_queue.append((water[0], water[1], 0))

    while water_queue:
        y, x, cnt = water_queue.popleft()

        for move in moves:
            if 0 <= y+move[0] < R and 0 <= x+move[1] < C and floor_timeline[y+move[0]][x+move[1]] == -1:
                #홍수 타임라인 설정
                floor_timeline[y + move[0]][x + move[1]] = cnt + 1
                water_queue.append((y + move[0], x + move[1], cnt + 1))

    #print(floor_timeline) #[[0, 1, 0], [3, 2, 1], [4, 3, 2]]

    #물이 다 흘러간후에도 -1이면 언제든지 갈 수 있는 곳
    for r in range(R):
        for c in range(C):
            if floor_timeline[r][c] == -1:
                floor_timeline[r][c] = 99999

    #S 시작
    visited = [[False for _ in range(C)] for i in range(R)]

    beaver_queue.append((S[0], S[1], 0))
    visited[S[0]][S[1]] = True

    while beaver_queue:
        y, x, cnt = beaver_queue.popleft()

        if y == D[0] and x == D[1]:
            answer = cnt
            break

        for move in moves:
            if 0 <= y+move[0] < R and 0 <= x+move[1] < C and cnt + 1 < floor_timeline[y+move[0]][x+move[1]] and not visited[y+move[0]][x + move[1]]:
                visited[y+move[0]][x + move[1]] = True
                beaver_queue.append((y + move[0], x + move[1], cnt + 1))

    if answer == -1:
        print('KAKTUS')
    else:
        print(answer)

