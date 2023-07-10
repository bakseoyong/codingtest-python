def find_root(i):
    global parent

    if i == parent[i]:
        return i
    else:
        return find_root(parent[i])

def solve():
    global parent
    n, m = map(int, input().split())

    parent = [-1 for _ in range(n)]
    arr = []
    for i in range(m):
        arr.append(list(map(int, input().split())))

    index = 1
    for a in arr:
        if parent[a[0]] == -1 and parent[a[1]] == -1:
            #신규
            parent[a[0]] = parent[a[1]] = a[0]
        elif parent[a[0]] != -1 and parent[a[1]] == -1:
            #갱신
            parent[a[0]] = parent[a[1]] = find_root(a[0])
        elif parent[a[1]] != -1 and parent[a[0]] == -1:
            #갱신
            parent[a[1]] = parent[a[0]] = find_root[a[1]]
        elif parent[a[0]] == parent[a[1]]:
            #사이클 발견
            print(index)
            return
        elif parent[a[0]] != parent[a[1]]:
            #병합
            r1 = find_root(a[0])
            r2 = find_root(a[1])
            rr1 = find_root(r1)
            rr2 = find_root(r2)

            if rr1 == rr2:
                parent[a[0]] = parent[a[1]] = rr1
            else:
                parent[a[1]] = rr1

            #병합되어진 노드들 갱신


        index += 1


if __name__ == '__main__':
    solve()