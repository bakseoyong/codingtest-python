def solution(operations):
    import math
    answer = []

    max_heap = [0 for i in range(1000001)]
    max_heap[0] = math.inf
    current_insert_nums = 0
    # heap_depth = 0 # log(current_insert_nums)
    # leaf_nodes_num = 2 ** heap_depth - 1

    def insert(number):
        nonlocal current_insert_nums
        current_insert_nums += 1
        max_heap[current_insert_nums] = number

        # 비교
        compare_index = current_insert_nums
        while max_heap[compare_index // 2] < max_heap[compare_index]:
            temp = max_heap[compare_index // 2]
            max_heap[compare_index // 2] = max_heap[compare_index]
            max_heap[compare_index] = temp
            compare_index = current_insert_nums // 2

    for operation in operations:
        if operation[0] == 'I':
            #insert
            inserts = operation.split()
            num = int(inserts[1])

            insert(num)


        elif operation == 'D 1':
            if current_insert_nums == 0:
                continue
            #최대값 제거
            max_heap[1] = 0
            max_heap[1] = max_heap[current_insert_nums]
            max_heap[current_insert_nums] = 0
            current_insert_nums -= 1
            #비교하면서 높이 조절하기
            current_loop_index = 1
            while True:
                if current_insert_nums >= current_loop_index * 2:
                    if max_heap[current_loop_index * 2] > max_heap[current_loop_index]:
                        temp = max_heap[current_loop_index]
                        max_heap[current_loop_index] = max_heap[current_loop_index * 2]
                        max_heap[current_loop_index * 2] = temp
                        current_loop_index *= 2
                elif current_insert_nums >= current_loop_index * 2 + 1:
                    if max_heap[current_loop_index * 2 + 1] > max_heap[current_loop_index]:
                        temp = max_heap[current_loop_index]
                        max_heap[current_loop_index] = max_heap[current_loop_index * 2 + 1]
                        max_heap[current_loop_index * 2 + 1] = temp
                        current_loop_index = current_loop_index * 2 + 1
                else:
                    break

        elif operation == 'D -1':
            if current_insert_nums == 0:
                continue
            #최소값 제거
            current_depth = int(math.log2(current_insert_nums)) + 1
            min_num = math.inf
            chg_index = math.inf
            for index in range(2 ** (current_depth - 1), current_insert_nums + 1): #2 ** current_depth):
                if min_num >= max_heap[index]: # 크거나 같은 이유 : 뒤에서 발견할 수록 땡기기 수월하기 떄문에
                    chg_index = index
                    min_num = max_heap[index]

            max_heap[chg_index] = 0
            current_insert_nums -= 1

            #옆칸으로 떙기기
            left_shift_nums = []
            for index in range(chg_index + 1, current_insert_nums + 1 + 1):# 이전 배열들은 nums를 한개 줄이기전 모습을 하고 있으므로
                left_shift_nums.append(max_heap[index])
                max_heap[index] = 0
            current_insert_nums -= len(left_shift_nums)

            for l in left_shift_nums:
                insert(l)


            # 1이면 1
            # 2이면 2 3
            # 3이면 4 5 6 7
            # 4이면 8 9 10 11 12 13 14 15

    max_answer = -math.inf
    min_answer = math.inf

    for i in range(1, current_insert_nums + 1):
        max_answer = max(max_answer, max_heap[i])
        min_answer = min(min_answer, max_heap[i])

    if max_answer == -math.inf and min_answer == math.inf:
        answer.append(0)
        answer.append(0)
        return answer

    print(max_answer, min_answer)
    answer.append(max_answer)
    answer.append(min_answer)
    return answer

if __name__ == '__main__':
    operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
    solution(operations)
    #
    # D 명령어가 올때만 삭제하면 된다. 그리고 최대값 최소값만 삽입시에 갱신해주면 된다.
    # 최대힙 최소힙 두개 두고
    # 삽입시에 둘 다 집어넣고
    # 삭제시에는 한 곳에만 해야되니까 일관성 문제가 생긴다.
    #
    # 일관성 어떻게 만들지
    # 최대 힙에서 뺐는데 그 값이 없다면 그냥 빼기
    #
    # 123 16 -5643
    #
    # 자체 힙을 제작하고 빼나가면 될 것 같다.
    # 백만개 모두 삽입 연산이라고 한다면 깊이는 17정도 될 것이고 17이 깊이라면 34번의 이하의 연산 안에서 가장 작은 값을 구할 수 있다.
    #
    # heapq 라이브러리 쓸 수 없는 이유는 저렇게 최솟값을 가져와야 하기 때문이다.
    #
    #
