def solution(n, m, before, after):
    # 행렬 변환 연산을 수행할 수 있는 자리 구하기 + 내 자리의 값이 다르다면 값 바꿔주기
    possible = []
    answer = 0

    for i in range(n):
        for j in range(m):
            #변환 연산을 수행할 수 있는 자리라면
            if (i + 2) < len(before) and (j + 2) < len(before[0]):
                possible.append((i, j))

    if len(possible) == 0:
        # 변환없이도 가능할 수 있다.
        for row in range(len(before)):
            if before[row] != after[row]:
                print(-1)
                return

        print(0)
        return answer

    # print(possible) # 잘 작동

    #내 자리의 값이 다르면 바꿔주기
    for x, y in possible:
        if before[x][y] == after[x][y]:
            continue
        else:
            answer += 1
            for i in range(x, x+3):
                for j in range(y, y+3):
                    if before[i][j] == '0':
                        before[i][j] = '1'
                    else:
                        before[i][j] = '0'

    #변환을 끝낸 후 전체 비교
    for row in range(len(before)):
        if before[row] != after[row]:
            print(-1)
            return

    print(answer)
    return answer




if __name__ == '__main__':
    n, m = map(int, input().split())

    before = [[] for _ in range(n)]
    after = [[] for _ in range(n)]

    for j in range(n):
        before[j] = list(input())

    for k in range(n):
        after[k] = list(input())

    solution(n, m, before, after)

    # print(n, m)
    # print(before)
    # print(after)
    # 3 4
    # ['0000', '0010', '0000']
    # ['1001', '1011', '1001']