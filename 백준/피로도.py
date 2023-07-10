def solution(a, b, c, m):
    time = 0
    current = 0
    score = 0
    while time < 24:
        time += 1

        if current + a <= m:
            score += b
            current += a
        elif current + a > m:
            if c >= current:
                current = 0
            else:
                current -= c
    print(score)

if __name__ == '__main__':
    a, b, c, m = map(int, input().split())

    solution(a, b, c, m)