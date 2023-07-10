def solution(n):
    if n == 0:
        print(0)
        return
    elif n == 1:
        print(1)
        return
    elif n == 2:
        print(2)
        return

    three_num = n // 3
    remain = n % 3
    answer = 1
    # 나머지가 2이면 마지막이 5니까 쪼개는게 더 이득
    # 나머지가 1일 경우이면 4니까 3 * 1 보다 4로 해서 곱하는게 이득
    # 나머지가 0이면 신경안씀
    for i in range(three_num - 1):
        answer = (answer % 10007) * 3

    if remain == 1:
        answer = (answer % 10007) * 4
    elif remain == 0:
        answer = (answer % 10007) * 3
    elif remain == 2:
        answer = (answer % 10007) * 6


    print(answer % 10007)


if __name__ == '__main__':
    n = int(input())

    solution(n)