import sys
sys.setrecursionlimit(10**6)

def dfs(index, recursive):
    global arr, discover, finished, matched
    if discover[index] == 0:
        discover[index] = recursive
        dfs(arr[index], recursive + 1)
    else:
        if not finished[index]:
            matched += recursive - discover[index]
    finished[index] = True

def solve():
    global arr, discover, finished, matched
    t = int(input())
    arr = []
    discover = []
    finished = []
    matched = 0
    for i in range(t):
        matched = 0
        n = int(input())

        arr = list(map(int, input().split()))
        arr.insert(0, 0)

        discover = [0 for _ in range(n + 1)]
        finished = [False for _ in range(n + 1)]

        for j in range(1, n + 1):
            if discover[j] == 0:
                dfs(j, 1)

        print(n - matched)





if __name__ == '__main__':
    solve()