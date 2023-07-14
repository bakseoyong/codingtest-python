def solve():
    n = int(input())

    arr = []
    num = []
    for i in range(n):
        arr.append(input())
        num.append(i+1)

    d = dict(zip(arr, num))
    # print(d)

    exist = [False for i in range(n+1)]
    now = 1
    arr2 = []
    answer = 0
    for i in range(n):
        ss = input()
        if d[ss] > now:
            answer += 1
            exist[d[ss]] = True
        elif d[ss] == now:
            exist[now] = True
            for j in range(now, len(exist)):
                if not exist[j]:
                    now = j
                    break

    print(answer)


if __name__ == '__main__':
    solve()