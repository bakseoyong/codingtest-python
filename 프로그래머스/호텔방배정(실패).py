# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# 시간 복잡도 O(N^2)
def solution1(k, room_number):
    answer = []

    reserved = [False for i in range(len(room_number) + 1)]
    #print(len(reserved))

    for r in room_number:
        if not reserved[r]:
            reserved[r] = True
            answer.append(r)
            continue
        elif reserved[r]:
            search_idx = r
            #print(search_idx)
            while reserved[search_idx]:
                search_idx += 1
            reserved[search_idx] = True
            answer.append(search_idx)
            continue

    print(answer)
    return answer



def solution2(k, room_number):
    answer = []

    # 이분탐색이 떠올랐다. 이유 : 전부 순회하므로 오랜 시간이 걸리니까 절반 절반 나눠서 진행하면 괜찮지 않을까 싶었다.
    # 틀린 이유 : visited에서 올라가야되기 때문에 절반 절반 나누면 중간에 빈 공간이 생길 수 있다.
    #
    # 그다음 서로소(Union - Find)가 떠올랐다. 이유 : 연결된 것들을 빠르게 넘어갈 수 있을것 같다.
    reserved = [False for i in range(len(room_number) + 1)]

    root_nodes = [t for t in range(1, k + 1)]
    print(root_nodes)

    return answer

def solution3(k, room_number):
    #자신이 호출된 수만큼 카운트 해서 저장하면 되겠다.
    answer = []

    visited = [0 for i in range(len(k) + 1)]
    # print(len(reserved))

    for r in room_number:
        if visited[r] == 0:
            visited[r] += 1
            answer.append(r)
            continue
        elif visited[r] != 0:
            #print("elif index is : ", r)
            search_idx = r
            # print(search_idx)
            # 0이 나올때 까지 점프
            while visited[search_idx + visited[search_idx]] != 0:
                #print("jump to next index : ", search_idx + visited[search_idx])
                search_idx = search_idx + visited[search_idx]
            visited[search_idx + visited[search_idx]] += 1
            answer.append(search_idx + visited[search_idx])
            continue

    #print(answer)
    return answer


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    room_number = [1, 3, 4, 1, 3, 1];
    solution3(10, room_number)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
