def solution(n, roads, cities):
    total = 0
    cost = 0
    current = 0
    drive = 0
    now_fuel_cost = 0
    #distance 총 거리 구하기 = O(N) = 10^6
    for road in roads:
        total += road

    cost = total * cities[0]
    current_cost = cities[0] * roads[0]
    now_fuel_cost = cities[0]
    drive = roads[0]

    for index in range(1, len(cities) - 1): #-1하는 이유. 마지막 도시의 주유소는 들릴 필요가 없기 떄문에
        if cost > current_cost + (total - drive) * cities[index]: #min(이전까지 최소값, 이번에 갱신하는 값)
            now_fuel_cost = cities[index]
            cost = current_cost + (total - drive) * cities[index]

        current_cost += now_fuel_cost * roads[index]

    print(cost)


if __name__ == '__main__':
    n = input()
    roads = list(map(int, input().split()))
    cities = list(map(int, input().split()))

    solution(n, roads, cities)