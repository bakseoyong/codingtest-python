def solution(n, m, arrs):
    colors = [1 for _ in range(n)]

    for arr in arrs:
        if arr[0] < arr[1]:
            colors[arr[1] - 1] = colors[arr[0] - 1] + 1
        else:
            colors[arr[0] - 1] = colors[arr[1] - 1] + 1

    for color in colors:
        print(color, end=' ')

if __name__ == '__main__':
    n, m = map(int, input().split())

    arrs = []

    for i in range(m):
        arrs.append(list(map(int, input().split())))

    solution(n, m, arrs)
    # print(arrs)
