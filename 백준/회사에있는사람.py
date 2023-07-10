def solution():
    print(1)

if __name__ == '__main__':
    n = int(input())
    d = {}

    for i in range(n):
        name, status = input().split()
        #print(name, status)

        if status == 'enter':
            d[name] = d.get(name, 1)
        elif status == 'leave':
            d.pop(name, 0)

    #정렬
    sort = sorted(d.items(), reverse=True)

    for item in sort:
        print(item[0])
