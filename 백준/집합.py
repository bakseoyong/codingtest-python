def solution():
    print(1)

if __name__ == '__main__':
    n = int(input())

    d = set()

    for i in range(n):
        inputs = input().split()
        if inputs[0] == 'add':
            d.add(inputs[1])
        elif inputs[0] == 'remove':
            d.discard(inputs[1])
        elif inputs[0] == 'check':
            if inputs[1] in d:
                print(1)
            else:
                print(0)
        elif inputs[0] == 'toggle':
            if inputs[1] in d:
                d.discard(inputs[1])
            else:
                d.add(inputs[1])
        elif inputs[0] == 'all':
            for j in range(1, 21):
                d.add(j)
        elif inputs[0] == 'empty':
            d.clear()

