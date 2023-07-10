if __name__ == '__main__':
    N = int(input())

    rooms = list(map(int, input().split()))

    B, C = map(int, input().split())

    # print(rooms)
    # print(B, C)

    # 감독관의 최소 수
    # 총감독관은 최소 1명씩 있어야 한다. 그래서 시험장마다 총감독관의 인원수 만큼 빼준다.
    # 부감독관 감시할 수 있는 인원수
    answer = 0

    # 백만에서 5빼면 999995 -> 142856.. -> 142857
    # 이렇게 하면 714290 나와야 되는데...


    for room in rooms:
        if room - B > 0:
            answer += 1
            temp = room - B
            answer += int(temp / C)
            #print(int(temp / C))
            if temp % C != 0:
                answer += 1
        else:
            answer += 1
            continue

    print(answer)