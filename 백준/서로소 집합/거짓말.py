def find(x):
    global parent
    if x == parent[x]:
        return x
    return find(parent[x])

def merge(p, q):
    global parent

    x = find(p)
    y = find(q)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y
def solve():
    global parent
    N, M = map(int, input().split())

    know = list(map(int, input().split()))
    party = []
    for _ in range(M):
        party.append(list(map(int, input().split())))

    if know[0] == 0:
        print(M)
        return

    parent = [i for i in range(0, N+1)]
    # print(parent)

    # print(know)
    # print(party)

    for i in range(1, len(know)):
        if i == 1:
            continue
        else:
            parent[know[i]] = parent[know[1]]
    # print(parent)

    for i in party:
        person = i[0]
        p = find(i[1])
        for j in range(2, 1 + person):
            q = find(i[j])
            if p != q:
                merge(i[1], i[j])

    # print(parent)

    final_parent = find(know[1])

    for i in range(1,N+1):
        if final_parent == find(i):
            parent[i] = final_parent

    # print(parent)

    answer = M
    for i in party:
        person = i[0]
        for j in range(1, 1 + person):
            if parent[i[j]] == final_parent:
                answer -= 1
                break

    print(answer)





if __name__ == '__main__':
    solve()