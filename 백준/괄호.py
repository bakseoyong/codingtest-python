if __name__ == '__main__':
    N = int(input())

    str = input()

    remain = 0

    for s in str:
        if s == '(':
            remain += 1
        else:
            remain -= 1

    remain으로 경우의수 구하기

