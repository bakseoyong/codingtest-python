
if __name__ == '__main__':
    N = int(input())

    SCVs = list(map(int, input().split()))

    dp = [[[0 for _ in range(61)] for _ in range(61)] for _ in range(61)]

    damages = [9, 3, 1]

    queue = []

    answer = 0

    arrs = []
    if N == 1:
        arrs.append(0)
        arrs.append(0)
        arrs.append(SCVs[0])
    elif N == 2:
        arrs.append(0)
        arrs.append(SCVs[0])
        arrs.append(SCVs[1])
    elif N == 3:
        arrs.append(SCVs[0])
        arrs.append(SCVs[1])
        arrs.append(SCVs[2])

    arrs.sort(reverse=True)
    dp[arrs[0]][arrs[1]][arrs[2]] = 0
    queue.append(arrs)
    isEnd = False

    while queue:
        A, B, C = queue.pop(0)

        availables = [(9, 3, 1), (9, 1, 3), (1, 3, 9), (1, 9, 3), (3, 1, 9), (3, 9, 1)]

        for a in availables:
            aA = max(A - a[0], 0)
            aB = max(B - a[1], 0)
            aC = max(C - a[2], 0)
            temps = [aA, aB, aC]
            temps.sort(reverse=True)

            if aA == 0 and aB == 0 and aC == 0:
                answer = dp[A][B][C] + 1
                isEnd = True
                break

            if dp[temps[0]][temps[1]][temps[2]] != 0:
                continue #큐니까 무조건 먼저 도달한게 더 짧을 것, 다시 왔다면 큐에 집어넣지 않고 pass
            else:
                dp[temps[0]][temps[1]][temps[2]] = dp[A][B][C] + 1
                queue.append(temps)

        if isEnd:
            break
    print(answer)


