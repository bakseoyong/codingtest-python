def solution(n, k):
    sum = k * (k + 1) / 2

    have = [0 for _ in range(k)]

    if n < sum:
        print(-1)
        return
    elif n >= sum:
        #시작
        for index in range(k): #sum = 6, k = 3인 경우 6, 7, 8 순회
            if index == 0:
                have[int(sum % k)] = k - 1
            else:
                have[int((sum + index) % k)] = k

    #정답찾기
    print(have[n % k])


if __name__ == '__main__':
    n , k = map(int, input().split())

    solution(n, k)