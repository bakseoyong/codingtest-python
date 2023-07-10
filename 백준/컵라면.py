import heapq

def solution():
    print(1)

if __name__ == '__main__':
    n = int(input())

    queue = []

    answer = 0

    #시간, 데드라인, 컵라면개수
    arrs = []

    for i in range(n):
        arrs.append(list(map(int, input().split())))

    arrs.sort(key= lambda x : (x[0], x[1]), reverse=True)

    current = arrs[0][0] #deadline
    next = 0
    answer += 0

    index = 0
    while current != 0:
        while current == arrs[index][0] and index < len(arrs):
            heapq.heappush(queue, arrs[index][1])
            index += 1

        #while문이 끊기면 시간대가 바뀜.
        next = arrs[index][0]

        for i in range(current - next):
            value = heapq.heappop(queue)
            answer += value

        current = next
