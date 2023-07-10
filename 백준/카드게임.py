def recursive(ss, ee):
    global dp, arr
    if dp[ss][ee] == -1:
        if ee - ss == 1: #리프 탐색
            dp[ss][ee] = max(dp[ss][ss], dp[ee][ee])

        if ss + 2 <= ee:
            if dp[ss + 2][ee] == -1:
                dp[ss + 2][ee] = recursive(ss + 2, ee)
            dp[ss][ee] = max(dp[ss][ee], dp[ss][ss] + dp[ss + 2][ee])

        if ee - 2 >= ss:
            if dp[ss][ee - 2] == -1:
                dp[ss][ee - 2] = recursive(ss, ee - 2)
            dp[ss][ee] = max(dp[ss][ee], dp[ee][ee] + dp[ss][ee - 2])

    return dp[ss][ee]




if __name__ == '__main__':
    global dp, arr
    T = int(input())

    for _ in range(T):
        N = int(input())

        arr = list(map(int, input().split()))

        dp = [[-1 for i in range(len(arr))] for j in range(len(arr))]

        for i in range(len(arr)):
            dp[i][i] = arr[i]

        is_first = True
        player1 = 0
        player2 = 0
        s = 0
        e = len(arr) - 1

        while s <= e:
            # print(dp)

            pick_start = dp[s][s]
            pick_end = dp[e][e]

            if s + 2 <= e:
                if dp[s + 2][e] == -1:
                    dp[s + 2][e] = recursive(s + 2, e)
                pick_start += dp[s+2][e]
            elif e - 2 >= s:
                if dp[s][e - 2] == -1:
                    dp[s][e - 2] = recursive(s, e - 2)
                pick_end += dp[s][e -2]

            if pick_start >= pick_end:
                if is_first:
                    player1 += dp[s][s]
                else:
                    player2 += dp[s][s]
                s += 1
            else:
                if is_first:
                    player1 += dp[e][e]
                else:
                    player2 += dp[e][e]
                e -= 1

            if is_first:
                is_first = False
            else:
                is_first = True

            # print(player1, player2)
        print(player1)





