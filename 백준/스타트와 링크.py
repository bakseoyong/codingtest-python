import math


def dfs(depth, idx):
    global min_diff, visited, graph, n

    if depth == n//2:
        power1, power2 = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    power1 += graph[i][j]
                elif not visited[i] and not visited[j]:
                    power2 += graph[i][j]
        min_diff = min(min_diff, abs(power1-power2))
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, i+1)
            visited[i] = False


def solve():
    global min_diff, visited, graph, n
    n = int(input())

    visited = [False for _ in range(n)]
    graph = [list(map(int, input().split())) for _ in range(n)]
    min_diff = math.inf

    dfs(0, 0)
    print(min_diff)

if __name__ == '__main__':
    solve()