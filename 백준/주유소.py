def solution(n, roads, cities):

    find_min_fuel = 1000000001
    use_fuel = 0

    for index in range(len(cities) - 1):
        find_min_fuel = min(find_min_fuel, cities[index])
        use_fuel += find_min_fuel * roads[index]
        #print(find_min_fuel, use_fuel)




    print(use_fuel)


if __name__ == '__main__':
    n = input()
    roads = list(map(int, input().split()))
    cities = list(map(int, input().split()))

    solution(n, roads, cities)