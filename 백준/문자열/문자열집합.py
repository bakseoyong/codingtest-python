def solve():
    n, m = map(int, input().split())

    arr1 = []
    arr2 = []
    for i in range(n):
        arr1.append(input())
    tuple(arr1)
    answer = 0
    for j in range(m):
        s = input()
        if s in arr1:
            answer += 1

    print(answer)

if __name__ == '__main__':
    solve()