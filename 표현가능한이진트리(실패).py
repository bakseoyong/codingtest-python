def solution(numbers):
    answer = []

    #이진트리로 표현할 수 있는가

    #dp 절대 안됨 10^15
    # 111이 되는지 확인하려면 2진수로 만들고 그게 포화트리에 포함되는가를 확인해야 한다.
    # len(numbers)도 10000이니까 순회하면서 하는게 맞는듯.
    #
    #
    # 10진수를 2진수로 바꿔보기
    #
    # 7 - 111(2)

    for number in numbers:
        alreadyAdded = False
        binary = format(number, 'b')

        print(len(binary))
        if len(binary) % 2 == 1: #홀수
            #포화트리인지 확인할 필요없이 짝수번쨰가 전부 1이면 가능 (인덱스로 하면 홀수번째)
            for index in range(0, len(binary)):
                if index % 2 == 1 and binary[index] == 0: #if조건에 두개가 들어가야지 index가 홀수이고 binary[index]가 0인지
                    answer.append(0)
                    alreadyAdded = True
                    break
            if not alreadyAdded:
                answer.append(1)
        else: #짝수
            #문자를 추가해줘야 한다.

            # 짝수 번째에 0이 나왔다면 1을 추가하고 다시 탐색을 이어나간다.
            # 근데도 또 짝수번째에 0이 나온다면 진짜 아닌거
            # (또 0이 나오면 포화트리에서 벗어나게 된다.)
            # 근데 1101은 또 되는이유는 같은 높이를 맞추면서 하나만 튀어나올 수 있기 때문에
            # => 안 되는 이유 : 0이 맨앞에 붙을 수가 없다. (101010 은 포화 트리지만 위 방식을 이용하면 식별 불가능)

            # 1을 집어 넣거나 0을 집어넣으면 다른 숫자가 되버린다!
            # 0은 1이 최초로 나오기 전까지만 넣을 수 있다. => 앞에 집어넣는 거랑 똑같다.
            # 근데 0을 두개 넣으면

            binary = '0' + binary
            for index in range(0, len(binary)):
                if index % 2 == 1 and binary[index] == 0:
                    answer.append(0)
                    alreadyAdded = True
                    break
            if not alreadyAdded:
                answer.append(1)

            #홀수를 만들었을때 짝수번째 인덱스들이 1을 가지고 있는지 확인해야 한다.



    #
    # 101010 <- 개수가 짝수니까 살을 붙여줄 수 있다. 맨왼쪽에 0 붙여주면 된다.
    #
    # -> 포화 트리면 0을 사이사이에 껴넣는게 가능
    # -> 포화 트리가 아니면 문자열(2진수)가 홀수가 되도록 만들어 줄 수 있다. 이미 홀수인데 포화트리가 아니면 추가해 줄 수 없음.
    # 1101111 <- 이건 포화트리가 아님 + 홀수 추가가 불가능
    #
    # 그렇다면 짝수일때는 추가가 가능할까 <- 어디에 추가할 수 있을지
    # 101010일때
    # (0)101010
    #
    # 1111111
    # 0101010
    # 0111110
    # 0101111
    # 0101110 -> 짝수개가 1이기만 하면 가능 홀수는 0이든 1이든 상관없음
    #
    # 탐색하면서 0을 집어넣었을때 짝수가 모두 1이면 성공


    print(answer)
    return answer

if __name__ == '__main__':
    numbers = [7, 42, 5]

    solution(numbers)