from itertools import combinations
def solve():
    n = int(input())

    strs = []
    for i in range(n):
        strs.append(''.join((sorted(input()))))

    print(len(set(strs)))




if __name__ == '__main__':
    solve()