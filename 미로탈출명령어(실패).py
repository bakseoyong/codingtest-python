def solution(n, m, x, y, r, c, k):
    answer = ''
    ready_answers = []

    moves = [(1, 0, "d"), (0, -1, "l"), (0, 1, "r"), (-1, 0, "u")]

    #현재 위치 , 현재 순회 횟수, 현재 까지의 문자열
    def dfs(c_n, c_m, r_n, c_c):
        if r_n > k:
            return

        #순회 횟수와 도착 좌표가 같다면
        if c_n == r and c_m == c and r_n == k:
            ready_answers.append(c_c)

        for move in moves:
            if 1 <= c_n + move[0] <= n:
                if 1 <= c_m + move[1] <= m:
                    if len(ready_answers) > 0:
                        return
                    dfs(c_n + move[0], c_m + move[1], r_n + 1, c_c + move[2])

    dfs(x, y, 0, "")

    if len(ready_answers) > 0:
        answer = ready_answers[0]
    else:
        answer = "impossible"
    return answer

if __name__ == '__main__':
    n, m, x, y, r, c, k = 3, 4, 2, 3, 3, 1, 5
    solution(n, m, x, y, r, c, k)

    #찾은 경로 들 중에서 사전순으로 배열 => dfs
