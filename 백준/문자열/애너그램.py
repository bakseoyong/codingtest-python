def recursive(now, finish, temp):
    global a
    if now >= finish:
        print(temp)
    else:
        for i in range(26):
            if a[i] > 0:
                a[i] -= 1
                recursive(now + 1, finish, temp + chr(i + 97))
                a[i] += 1

def solve():
    global a
    N = int(input())

    for i in range(N):
        str = sorted(input())

        a = [0 for _ in range(26)]
        for s in str:
            a[ord(s) - 97] += 1
        recursive(0, len(str), '')


if __name__ == '__main__':
    solve()

