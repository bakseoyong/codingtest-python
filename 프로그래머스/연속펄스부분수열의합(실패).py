def solution(sequence):
    answer = 0

    # plus_odd_sequence = [] (0)
    # minus_odd_sequence = [] (1)
    pulse_sequence = [[], []]


    for index in range(len(sequence)):
        if(index % 2 == 1):
            pulse_sequence[0].append(sequence[index])
            pulse_sequence[1].append(-sequence[index])
        else:
            pulse_sequence[0].append(-sequence[index])
            pulse_sequence[1].append(sequence[index])

    print(pulse_sequence[0])
    print(pulse_sequence[1])
    # 저걸 규칙으로 만들어야 됨...
    # while True:
    # 홀수이면 왼쪽에서 오른쪽으로 진행
    # 짝수이면 오른쪽에서 왼쪽으로 진행
    print("pulse len is : ", len(pulse_sequence))
    for s in pulse_sequence:
        print("s is : " + str(s[0]))
        temp = (s[0], 0, 0)
        sum = s[0]

        for index in range(1, len(s)):
            print(index)
            sum += s[index]
            temp = max((sum, 0, index), temp)
            print(temp)

        print(temp)
        looping = 0
        while True:
            print(looping)
            before_temp = temp
            sum = before_temp[0]
            if looping % 2 == 1:
                for index in range(before_temp[2], before_temp[1] - 1, -1):
                    sum -= s[index]
                    temp = max((sum, before_temp[1], index - 1), temp)
            else:
                # temp를 써야지
                # 2(3 - 1)번 인덱스 까지 조회했으니까 이제 왼쪽여서 줄여들어와야지
                for index in range(before_temp[1], before_temp[2] + 1):
                    print(index)
                    sum -= s[index]
                    temp = max((sum, index + 1, before_temp[2]), temp)

                #0부터 3이면 3 + 1해서 3까지 보는게 맞다.
            # 그래서 이제 temp랑 비교를 해 볼 차례
            # before_temp가 더 크면 더이상 순회를 반복하지 않고 before_temp를 가장 큰 값으로 사용하면 된다.
            # less eqaul이면 그래도 한 번더 순회 돌리기
            if(before_temp >= temp):
                break

            looping += 1
            print(temp)


        print(temp)

    return answer

if __name__ == '__main__':
    sequence = [2, 3, -6, 1, 3, -1, 2, 4]
    solution(sequence)

    # 50만건이고
    # 투포인터 방식은 못씀
    #
    # 펄스 수열과 곱했을때 최대값이 나오게 하기?
    #
    # 펄수 수열 고르는 법
    # : 짝수 펄스, 홀수 펄스 둘 다 곱해서 값 비교해보기
    #
    # 가장 합이 큰 부분 수열을 구한 다음에
    # 짝수 펄스, 홀수 펄스 곱해서 비교하기
    #
    # [2, 3, -6, 1, 3, -1, 2, 4]
    # 짝수 펄스 곱한 짝수_purse_list = [2, -3, 6, -1, 3, 1, 2, -4]
    # 홀수 펄스 곱한 홀수_purse_list = [-2, 3, 6, 1, -3, 1, -2, 4]
    #
    # 이래도 되는 이유 : 어떤 인덱스에서 잘라도 저 둘 중 하나일 것이기 때문에
    #
    # sequence = [2, 3, -6, 1, 3, -1, 2, 4]
    #
    # 부분 수열의 합이니까 누적합 해서 dp[i] - dp[j] 하면 될 것 같은데?
    # 50만번^2 하면 시간초과
    #
    # max
    # 2 (2)
    # -1(2, -3)
    # 5(2, -3, 6)
    # 4(2, -3, 6, -1)
    # 7(2, -3, 6, -1, 3)
    # 8(2, -3, 6, -1, 3, 1)
    # 10(2, -3, 6, -1, 3, 1, 2) <- 가장 큰 연속 수열 <- 여기서 왼쪽 줄이기
    # 6(2, -3, 6, -1, 3, 1, 2, -4)
    #
    # 8(-3, 6, -1, 3, 1, 2)
    # 11(6, -1, 3, 1, 2) <- 가장 큰 연속 수열 <- 여기서 오른쪽 줄이기
    # 5(-1, 3, 1, 2)
    # 6(3, 1, 2)
    # 3(1, 2)
    # 2(2)
    #
    # 9(6, -1, 3, 1) <- 가장 큰 연속 수열 <- 이전 보다 크지 않다. <- 반복 종료, 이전 값 (11) 사용하기
    # 8(6, -1, 3)
    # 5(6, -1)
    # 6(6)

    # 이 과정을 반복하는 걸 코드로 짜기
