def solution(n, arr):
    answer = []

    for index in range(len(arr) - 1, -1, -1):
        #print(index)
        answer.insert(arr[index], index + 1)

    for a in answer:
        print(a, end= ' ')





if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    solution(n, arr)