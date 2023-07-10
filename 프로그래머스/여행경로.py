tickets = []
used = []
answer = []

def solution(tickets):
    global answer, used
    used = [False for _ in range(len(tickets))]

    # 정렬
    tickets.sort(key=lambda x: x[1])
    print(tickets)

    # dfs
    def dfs(new_dep):
        global answer, used
        for index, ticket in enumerate(tickets):
            dep, arr = ticket
            if not used[index] and dep == new_dep:
                used[index] = True
                answer.append(arr)
                dfs(arr)
                break

    # 순회할떄 앞에있는게 무조건 사전순으로 앞서니까 DFS 돌리기
    for index, ticket in enumerate(tickets):
        dep, arr = ticket[0], ticket[1]

        if dep == 'ICN':
            used[index] = True
            answer.append('ICN')
            answer.append(arr)
            dfs(arr)
            break

    print(answer)
    return answer

if __name__ == '__main__':
    tickets = [["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]


    solution(tickets)