def solution(numbers):
    answer = []

    #1. 포화 이진 트리의 원소 개수는 2^n - 1개 이다.
    #2. 자식 노드가 1이라면 부모 노드도 무조건 1이여야 한다.
    for number in numbers:
        binary = format(number, 'b')

        full_binary_tree_nodes_depth = 1
        full_binary_tree_nodes_num = 1
        # 포화 이진 트리 원소 개수와 불일치 하다면 0을 앞에 더한다 ( 중간, 뒤에 더하면 숫자가 바뀜 )
        while full_binary_tree_nodes_num < len(binary):
            full_binary_tree_nodes_depth += 1
            full_binary_tree_nodes_num = pow(2, full_binary_tree_nodes_depth) - 1

        for loop in range(full_binary_tree_nodes_num - len(binary)):
            binary = '0' + binary

        #print(binary)

        #분할정복
        def algo(front, end):
            if front >= end:
                return binary[front]

            mid = (front + end) // 2
            a = algo(front, mid - 1)
            b = algo(mid + 1, end)
            #print(a, b)

            if a == '-1' or b == '-1':
                return '-1'

            if a == '1' or b == '1':
                #print("mid is : " + binary[mid])
                if binary[mid] == '1':
                    return binary[mid]
                else:
                    return '-1'

        result = algo(0, len(binary) - 1)

        if result == '-1':
            answer.append(0)
        else:
            answer.append(1)

        #분할



    print(answer)

    return answer


if __name__ == '__main__':
    numbers = [63, 111, 95]

    solution(numbers)