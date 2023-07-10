def solution():

    print(1)


if __name__ == '__main__':
    K = int(input())
    N = 0
    for i in range(0, 21):
        if K <= 2 ** i:
            N = i
            break

    min_pow = 0

    for i in range(N, -1, -1):
        if K - 2 ** i > 0:
            K -= 2 ** i
            continue
        elif K - 2 ** i < 0:
            continue
        elif K - 2 ** i == 0:
            min_pow = i
            break

    print(2 ** N, N - min_pow)