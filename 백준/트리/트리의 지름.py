import sys

sys.setrecursionlimit(10**6)

tree = [[] for _ in range(10001)]
answer = 0
def recursive(now):
    global answer, tree
    if len(tree[now]) == 0:
        return 0

    temp = []
    for i in range(len(tree[now])):
        b, c = tree[now][i][0], tree[now][i][1]
        temp.append(recursive(b) + c)

    temp.sort(reverse=True)
    # 전체 트리가 한 노드로만 이루어질 경우 해당 코드 없으면 틀렸습니다.
    if len(temp) == 1:
        answer = max(answer, temp[0])

    if len(temp) >= 2:
        answer = max(answer, temp[0] + temp[1])

    return temp[0]



def solve():
    global answer, tree
    n = int(input())

    for i in range(n - 1):
        a, b, c = map(int, input().split())
        tree[a].append((b, c))

    recursive(1)

    print(answer)



if __name__ == '__main__':
    solve()