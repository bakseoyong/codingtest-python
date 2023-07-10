def solution(n, arr):
    # 6 x 6 - 2차원 배열
    # dp[카운트, 현재 맥스값]
    dp = [[] for _ in range(n + 1)] #max값이 n일테니까

    print(dp)
    #그 다음 순회를 하면서 dp값을 갱신시킨다.
    for a in arr:
        #dp[1] 에는 4가 들어감. 그 다음 이전 값들 중엣
        dp[1].append(a)






if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().split()))

    # print(arr)
    solution(n, arr)

