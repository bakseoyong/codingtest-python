#실패
def solution(food_times, k):
    answer = 0

    dic = {}

    for index in range(len(food_times)):
        dic.setdefault(food_times[index], [])
        dic[food_times[index]].append(index)

    sorted_dict = dict(sorted(dic.items()))

    remain_foods_num = len(food_times)
    remain_foods_index = 0

    for sd in sorted_dict:
        if sd * remain_foods_num <= k:
            k -= sd * remain_foods_num
            remain_foods_num -= 1
            remain_foods_index += 1
        else:
            #남은 음식중에 k번째 인덱스가 정답이다.
            #heapq 사용하면 되겠다.

    return answer

# food_times 의 길이는 1 이상 200,000 이하이다.
# food_times 의 원소는 1 이상 100,000,000 이하의 자연수이다.
# k는 1 이상 2 x 10^13 이하의 자연수이다.

# 백만, 백만, 백만
# 274231번째
#
# 274231 / 3 = 91410 ... 1 -> 1번
#
# 백만, 만, 백만
# 274231번째
#
# 274231 / 3 = 91410 > 10000 (가장 작은 값 탐색에 20만회씩 거린다.)
#
# 274231 - 30000 = 244231
# 244231 / 2 =
#
# => 오름차순 정렬하기
# 만, 백만, 백만
# 백만일때 인덱스를 트리구조로 2, 3 번이 있다고 노드로 저장하고
# 나중에 마지막 단계가 되었을때 마지막 순서들을 전부 가져와 정렬해서 몇번째인지 선택하면 되겠다.


def solution2(food_times, k):
    union find 알고리즘을 사용하면 되지 않을까?

    다음으로 넘어가기

if __name__ == '__main__':
    food_times = [1, 10000000000, 1000000]
    k = 5

    solution(food_times, k)