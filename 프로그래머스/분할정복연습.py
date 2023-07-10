arrs = [1, 2, 3, 40, 5, 6, 7, 8, 9]

def solution(front, end):
    #print(front, end)
    if front >= end:
        #print(front)
        return arrs[front]

    mid = (front + end) // 2
    a = solution(front, mid)
    b = solution(mid + 1, end)

    if a > b:
        return a
    else:
        return b


if __name__ == '__main__':
    answer = solution(0, len(arrs) - 1)
    print(answer)
