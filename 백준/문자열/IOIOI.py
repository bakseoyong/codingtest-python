
def solve():
    N = int(input())
    M = int(input())
    S = input()
    answer, i, count = 0, 0, 0

    while i < (M - 1):
        str = S[i:i+3]
        if str == 'IOI':
            i += 2
            count += 1
            if count == N:
                answer += 1
                count -= 1
        else:
            i += 1
            count = 0

    print(answer)

if __name__ == '__main__':
    solve()