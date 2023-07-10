import math

def solve():

    r = int(input())

    for i in range(r):
        answer = math.inf
        row = [0, 0, 0, 0, 0, 0]
        col = [0, 0, 0, 0, 0, 0]

        for j in range(3):
            a, b = map(int, input().split())
            row[j] = col[j + 3] = a
            col[j] = row[j + 3] = b

        # 가로 1개, 세로 3개
        for k in range(6):
            for l in range(6):
                for m in range(6):
                    if m % 3 == k % 3 or m % 3 == l % 3 or k % 3 == l % 3:
                        continue

                    width = max(row[k], row[l], row[m])
                    height = col[k] + col[l] + col[m]
                    answer = min(answer, width * height)

        # 가로 1개, 세로 2개
        for k in range(6):
            for l in range(6):
                for m in range(6):
                    if m % 3 == k % 3 or m % 3 == l % 3 or k % 3 == l % 3:
                        continue

                    width = max(row[k], row[l] + row[m])
                    height = max(col[k] + col[l], col[k] + col[m])
                    answer = min(answer, width * height)

        print(answer)

if __name__ == '__main__':

    solve()