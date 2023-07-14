def solve():
    n = int(input())

    dictionary = dict()
    encodingg = []
    for i in range(n):
        alphabet, encoding = input().split()
        dictionary[encoding] = alphabet
        encodingg.append(encoding)
    tuple(encodingg)
    encoding_seq = input()

    # print(dictionary["111"])
    answer = ''
    i = 0
    temp = 1
    while i < len(encoding_seq):
        str = encoding_seq[i : i+ temp]
        if str in encodingg:
            answer += dictionary[encoding_seq[i:i + temp]]
            i += temp
            temp = 1
        else:
            temp += 1


    print(answer)

if __name__ == '__main__':
    solve()