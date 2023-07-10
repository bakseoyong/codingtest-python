def solution(n, roads, sources, destination):
    answer = []

    visited = [[False] * (n + 1) for _ in range(n + 1)]
    distances = [[500000] * (n+1) for _ in range(n + 1)]

    for i in range(1, n+1):
        distances[i][i] = 0
        visited[i][i] = True

    #거리 집어넣기
    for road in roads:
        distances[road[0]][road[1]] = 1
        distances[road[1]][road[0]] = 1

    from collections import deque
    queue = deque()
    queue.append(destination)
    visited[destination][destination] = True

    while len(queue) > 0:
        vertex = queue.popleft()
        print(vertex)

        for index in range(1, n + 1):
            if distances[vertex][index] != 500000 and not visited[vertex][index]:
                distances[destination][index]\
                    = min(distances[destination][vertex] + distances[vertex][index], distances[destination][index])
                queue.append(index)
                visited[vertex][index] = True
                visited[index][vertex] = True

        #1,2 1,4 2,4 2,5 4,5

    for source in sources:
        if distances[destination][source] == 500000:
            distances[destination][source] = -1

    return answer

if __name__ == '__main__':
    n = 5
    roads = [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]]
    sources = [1, 3, 5]
    destination = 5

    solution(n, roads, sources, destination)
