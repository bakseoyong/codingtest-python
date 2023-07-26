import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def recursive(temp):
    if len(temp) <= 0:
        return

    top = temp[0]

    if len(temp) > 1:
        for i in range(1, len(temp) + 1):
            if temp[i] > top:
                tempL = temp[1:i]
                tempR = temp[i:]
                break
            else:
                tempL = temp[1:]

        recursive(tempL)
        recursive(tempR)
    print(top)

def solve():
    arr = []
    while True:
        try:
            a = int(input())
            arr.append(a)
        except:
            break

    recursive(arr[:])


if __name__ == '__main__':
    solve()
