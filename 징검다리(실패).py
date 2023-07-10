def solution(distance, rocks, n):
    answer = 0

    #정렬
    rocks.sort()

    #이진 탐색하는 기준을 바꿔야 한다.
    해당 거리를 계산하는데 얼마나 많은 바위를 삭제해야 하는가
    (0(left) + distance(right)) / 2 의 길이를 유지하려고 하는데 n보다 많은 바위를 없앤다면 기준을 줄이고 (left = mid + 1)
    n보다 적은 바위를 없앤다면 기준을 늘린다 (right = mid - 1)

    이게 되는게 신기한데...
    바위 위치만 바꿔도 안될것 같은데 되는게 신기하다.


    return answer

if __name__ == '__main__':
    distance = 25
    rocks = [2, 14, 11, 21, 17]
    n = 2

    solution(distance, rocks, n)