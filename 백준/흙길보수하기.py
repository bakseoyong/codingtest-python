if __name__ == '__main__':
    N, L = map(int, input().split())

    waters = []

    for _ in range(N):
        waters.append(list(map(int, input().split())))

    # print(waters) #[[1, 6], [13, 17], [8, 12]]

    waters.sort()

    # print(waters) #[[1, 6], [8, 12], [13, 17]]
    for index, water in enumerate(waters):
        start, end = water

        diff = end - start

        L_num = diff // L + 1
        remain = L * L_num - diff

        remain -= 1

        #remain이 1이면
        next_start, next_end = waters[index + 1]

        if next_start - end <= remain:
            waters[index + 1] = [next_start + , next_end]



