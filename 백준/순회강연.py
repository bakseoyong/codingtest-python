if __name__ == '__main__':
    n = int(input())

    arrs = []

    for _ in range(n):
        arrs.append(list(map(int, input().split())))

    #print(arrs)

    arrs.sort(key=lambda x : (-x[1], -x[0]))

    #print(arrs)

    now_day = 0
    answer = 0
    now_search_index = 0
    visited = [False in range(n)]

    for index, arr in enumerate(arrs):
        if now_day != arr[1]:
            #일단 현재 걸 now_max로 잡는다 ( 자신의 날짜 중에서는 가장 높은 값이기 때문에
            now_max = arr[0]
            #그리고 자신의 앞들 것 들 중에 방문하지 않은거랑 비교한다.
            temp_max_index = index
            for i in range(index, -1, -1):
                if now_max <= arr[i][0] and not visited[i]:
                    temp_max_index = i
                    now_max = arr[i][0]
            visited[temp_max_index] = True

            #탐색이 끝나고 맥스값 사용





            now_day = arr[1]

    print(answer)


