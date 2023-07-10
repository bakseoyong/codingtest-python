if __name__ == '__main__':
    N = int(input())
    arrs = []

    for _ in range(N):
        arrs.append(int(input()))

    arrs.sort()

    now = arrs[0]
    answer = 0
    for index in range(1, len(arrs)):
        now += arrs[index]
        answer += now

    print(answer)
