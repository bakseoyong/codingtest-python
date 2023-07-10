strs = []
moves = [[-1, 0], [1, 0], [0, 1], [0, -1]]
r = 0
c = 0
answer = 0

def solution(current_row, current_col, visited, cnt):
    global strs, moves, r, c, answer

    #재귀를 통해 넘어왔다는 것은 현재까지는 문자열이 서로 겹치지 않고 진행되고 있음을 의미하므로
    answer = max(answer, cnt)

    # print(strs) # ['CAAB', 'ADCB']
    # 상 하 좌 우 한번씩 순회
    for move in moves:
        if 0 <= current_row + move[0] < r and 0 <= current_col + move[1] < c:
            # 방문하지 않은 문자열일때 if문 통과
            if not visited[ord(strs[current_row + move[0]][current_col + move[1]]) - ord('A')]:
                visited[ord(strs[current_row + move[0]][current_col + move[1]]) - ord('A')] = True
                solution(current_row + move[0], current_col + move[1], visited, cnt + 1)
                visited[ord(strs[current_row + move[0]][current_col + move[1]]) - ord('A')] = False



if __name__ == '__main__':
    r, c = map(int, input().split())

    strs = [[] for _ in range(r)]

    for i in range(r):
        strs[i] = input()

    visited = [False for _ in range(26)]
    # 7 7 7 5 = 26개
    visited[ord(strs[0][0]) - ord('A')] = True
    #print(visited)


    # print(visited)

    solution(0, 0, visited, 1)

    print(answer)