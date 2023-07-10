"""
해당 문제를 추천하지 않습니다.
알고리즘 스킬보다는 생각에 의존하는 문제인 것 같습니다.
98%에서 틀렸는데 더 하고 싶은 욕심이 안생겨 그만뒀습니다.
"""

def solve():
    n = int(input())

    arr = list(map(int, input().split()))

    arr.sort()

    #print(arr)
    first = second = -1
    index = 0

    while index < len(arr):
        alone = False
        if first != second:
            alone = True

        if arr[index] != first + 1:
            print(0)
            return
        first = arr[index]
        index += 1
        if alone:
            continue

        if index >= len(arr):
            break
        else:
            if arr[index] != first:
                continue
            else:
                second = arr[index]
                index += 1

    if second == -1:
        print(2)
        return
    #print(first, second)

    #if first + 1 + second + (0 if second == 0 else 1):
    if second == 0:
        print(4)
        return
    print((2 ** (second + 1)) * (2 if first > second else 1))


if __name__ == '__main__':
    solve()
