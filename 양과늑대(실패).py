from collections import deque

result = 0

def solution(info, edges):
    global result
    answer = 0

    sheep, wolf = 1, 0

    visitable = deque([])
    isVisited = [False for _ in range(len(info) + 1)]
    isVisited[0] = True

    for edge in edges:
        if edge[0] == 0:
            visitable.append(edge[1])

    for visit in visitable:
        if not isVisited[visit]:
            node = visit
            recursion(sheep, wolf, visitable, node, isVisited)

    # dp? 이유 : DFS로 풀려면 구현하기 까다라옴. 깊이대로 들어가는게 아니라 따른 노드도 왔다가
    # dp : 계속해서 더 나은 값으로 갱신 할 수 있기 때문에
    # 0을 통해 1에 도착하는 거랑 0-2에서 1로 오는거랑 0-2-5해서 1로 오는거랑
    #
    # 재귀함수로 풀기
    # 이번 회귀에서 온 노드가 양과 늑대의 개수가 똑같아 진다면 더 이상 가지 말기 return
    # 이번 회귀에서 온 노드가 양이 더 많을시 일단 진행
    # 파라미터로 받아온 방문 가능한 루트 + 내가 지금 신규로 갈 수 있는 루트를 더한 큐를 저장한다.
    # 이걸 인자로 전달하면서 다음 회귀 진행

    #내가 작성한 재귀함수의 문제점 : 다음 회귀로 넘어갈때 기존에 갈 수 있는 곳을 같이 안 들고 간다.



    print(result)
    return answer


def recursion(sheep, wolf, visitable, current_node, isVisited):
    global result

    isVisited[current_node] = True

    if info[current_node] == 1:
        wolf += 1
    else:
        sheep += 1

    if sheep <= wolf:
        return

    result = max(result, sheep)

    for edge in edges:
        if edge[0] == current_node:
            visitable.append(edge[1])

    for visit in visitable:
        if not isVisited[visit]:
            node = visit
            recursion(sheep, wolf, visitable, node, isVisited)

if __name__ == '__main__':
    info = [0,1,0,1,1,0,1,0,0,1,0]
    edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]

    solution(info, edges)