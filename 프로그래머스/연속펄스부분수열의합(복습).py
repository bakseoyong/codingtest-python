def solution(sequence):
    answer = 0

    pulse = [[1, -1], [-1, 1]]

    for p in pulse:
        dp = [0] * len(sequence)
        dp[0] = sequence[0] * p[0]

        for index in range(1, len(sequence)):
            if index % 2 == 1:
                dp[index] = max(dp[index - 1] + sequence[index] * p[1], sequence[index] * p[1])
            else:
                dp[index] = max(dp[index - 1] + sequence[index] * p[0], sequence[index] * p[0])

            answer = max(answer, dp[index])

    #print(answer)
    return answer

if __name__ == '__main__':
    sequence = [2, 3, -6, 1, 3, -1, 2, 4]

    solution(sequence)
