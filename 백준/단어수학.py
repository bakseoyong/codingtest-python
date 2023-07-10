if __name__ == '__main__':
    N = int(input())

    arrs = []

    for _ in range(N):
        arrs.append(input())

    # len(arr) 순으로 배열
    arrs.sort(key= lambda x: len(x), reverse=True)

    # print(arrs) #정렬 성공
    now_search_index = len(arrs[0]) - 1
    now_max_num = 9

    while now_search_index >= 0:
        this_loop_available_chars = []

        #우선 경합할 수 있는 char 들 전부 집어넣기
        for arr in arrs:
            if len(arr) >= now_search_index:
                this_loop_available_chars.append(arr[now_search_index])

        # 한 개라면 그냥 now_max_num 주고 넘겨버리기
        if len(this_loop_available_chars) == 1:
            change_char = this_loop_available_chars[0]

            for arr in arrs:
                arr.replace(change_char, now_max_num)

            now_max_num -= 1
        else:
            #경합 시작. temp_search_index = now_search_index - 1로 집어넣고 순회를 돌린다.
            # temp_max_num = now_max_num으로 할당한다.
            # temp_search_index에서 this_loop_available_chars안에 있는 char를 먼저 찾아내면 그 char를 temp_max_num 으로 넣고
            # now_max_num - temp_max_num 의 개수만큼 temp_search_index로 탐색이 되어 빠져나간것이기 때문에

        if now_search_index == 0:
            #아직 숫자가 안 된 것들 전부 집어넣어서 1씩 줄이기



