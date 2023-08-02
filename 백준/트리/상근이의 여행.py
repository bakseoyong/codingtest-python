def solve():
    for _ in range(int(input())):
        N, M = map(int, input().split())
        for _ in range(M):
            u, v = map(int, input().split())
        print(N - 1)

if __name__ == '__main__':
    solve()