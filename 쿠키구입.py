def solution(cookie):
    answer = 0

    for standard_line in range(len(cookie) - 1):
        two_pointer_left = standard_line
        two_pointer_right = standard_line + 1

        left_sum = cookie[two_pointer_left]
        right_sum = cookie[two_pointer_right]
        while True:
            if left_sum == right_sum:
                answer = max(answer, left_sum)

            if left_sum >= right_sum:
                if two_pointer_right == len(cookie) - 1:
                    break
                else:
                    two_pointer_right += 1
                    right_sum += cookie[two_pointer_right]
            elif left_sum <= right_sum:
                if two_pointer_left == 0:
                    break
                else:
                    two_pointer_left -= 1
                    left_sum += cookie[two_pointer_left]

    return answer


if __name__ == '__main__':
    cookie = [1, 1, 2, 3]
    solution(cookie)

    # #방법 1
    #
    # 1 2 3 4 5 6 7 8 9 10
    # 기준점을 세우고 거기서 좌 우로 이동하면서 값이 같은지 확인할 것 같아
    # 경계선을 두고 투포인터 알고리즘을 사용해서 이동시켜 보자
    # 종료 조건 : 한 쪽 끝까지 이동했는데 합이 안맞을경우(끝까지 간 쪽이 더 작아야됨)
    # 2000 * 2000 = 4000000
    #
    # [0, middle], (middle, len(cookie))
    #
    # #방법 2
    # 동적 프로그래밍
    # 누적합을 구한다음에 왼쪽 , 기준선, 오른쪽 기준으로 빼나가는것
    # 4000000 * 2000 = 8000000000 안되겠다.
    #
    # => 둘 이 비슷해 보인다.
    #
