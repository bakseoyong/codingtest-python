from sys import stdin

if __name__ == '__main__':
    N = int(input())

    flowers = []

    for _ in range(N):
        flowers.append(list(map(int, stdin.readline().split())))

    #print(flowers)

    before_date_month = 3
    before_date_day = 1

    flowers.sort(key= lambda x : (-x[2], -x[3]))
    #print(flowers)
    isError = False
    answer = 0

    while before_date_month < 11 or (before_date_month == 11 and before_date_day < 31):
        temp_answer = answer
        if answer > N:
            print(0)
            isError = True
            break

        for start_month, start_day, end_month, end_day in flowers:
            if start_month < before_date_month or (start_month == before_date_month and start_day <= before_date_day):
                before_date_month = end_month
                before_date_day = end_day
                answer += 1
                break

        if temp_answer == answer:
            print(0)
            isError = True
            break


    if not isError:
        print(answer)


