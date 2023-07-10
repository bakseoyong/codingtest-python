import math

if __name__ == '__main__':
    answer = 0
    N = int(input())

    v = []

    for _ in range(N):
        v.append(list(map(int, input().split())))

    # print(v)


    while len(v) > 1:
        min_multiple = math.inf
        index = -1

        for i in range(len(v) - 1):
            multiple = v[i][0] * v[i + 1][1]

            if min_multiple > multiple:
                min_multiple = multiple
                index = i

        answer += v[index][0] * v[index][1] * v[index + 1][1]
        v.insert(index, [v[index][0], v[index+1][1]])
        v.pop(index + 1)
        v.pop(index + 1)
        #print(v)

    print(answer)



