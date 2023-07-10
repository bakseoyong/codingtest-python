if __name__ == '__main__':
    N = int(input())

    inputs = list(map(int, input().split()))

    combinations_four = 301
    combinations_four = min(combinations_four, inputs[0] + inputs[3] + inputs[4])
    combinations_four = min(combinations_four, inputs[0] + inputs[1] + inputs[2])
    combinations_four = min(combinations_four, inputs[0] + inputs[1] + inputs[3])
    combinations_four = min(combinations_four, inputs[0] + inputs[2] + inputs[4])

    combinations_four = min(combinations_four, inputs[5] + inputs[1] + inputs[3])
    combinations_four = min(combinations_four, inputs[5] + inputs[1] + inputs[2])
    combinations_four = min(combinations_four, inputs[5] + inputs[3] + inputs[4])
    combinations_four = min(combinations_four, inputs[5] + inputs[4] + inputs[2])

    combinations_three = 301
    #12케이스 중 최솟값
    combinations_three = min(combinations_three, inputs[0] + inputs[2])
    combinations_three = min(combinations_three, inputs[0] + inputs[4])
    combinations_three = min(combinations_three, inputs[0] + inputs[3])
    combinations_three = min(combinations_three, inputs[0] + inputs[1])

    combinations_three = min(combinations_three, inputs[5] + inputs[2])
    combinations_three = min(combinations_three, inputs[5] + inputs[4])
    combinations_three = min(combinations_three, inputs[5] + inputs[3])
    combinations_three = min(combinations_three, inputs[5] + inputs[1])

    combinations_three = min(combinations_three, inputs[4] + inputs[3])
    combinations_three = min(combinations_three, inputs[4] + inputs[2])
    combinations_three = min(combinations_three, inputs[1] + inputs[3])
    combinations_three = min(combinations_three, inputs[1] + inputs[2])
    #print(combinations_three)

    combinations_one = 301
    combinations_one_max = 0
    for i in inputs:
        combinations_one = min(combinations_one, i)
        combinations_one_max = max(combinations_one_max, i)

    if N == 1:
        sum = 0
        for i in inputs:
            sum += i
        print(sum - combinations_one_max)
    else:
        sum = 0
        sum += combinations_four * 4
        #print(sum)
        sum += combinations_three * ( (N - 2) * 4 + 4 * (N - 1) )
        #print(sum)
        sum += combinations_one * (N ** 3 - 4 - ((N - 2) * 4 + 4 * (N - 1)) - ((N - 2) * (N - 2) * (N - 1)))
        #print(sum)
        print(sum)