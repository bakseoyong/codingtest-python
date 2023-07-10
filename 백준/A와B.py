if __name__ == '__main__':
    S = input()
    T = input()

    sequences = set()
    sequences.add(T)

    while len(T) > 0:
        if T[len(T) - 1] == 'A':
            T = T[:len(T) - 1]
        else:
            temp = list(T[:len(T) - 1])
            temp.reverse()
            T = ''.join(temp)

            # T = ''.join(list(T[:len(T) - 1]).reverse())
        sequences.add(T)

    #print(sequences)

    if S in sequences:
        print(1)
    else:
        print(0)

