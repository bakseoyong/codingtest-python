import copy


def solution(n, stocks):

    dc = copy.deepcopy(stocks)
    dc.sort(reverse=True)

    #print(dc) # 10 ^6 * 6
    current_sort_index = 0
    buy_stock_num = 0
    buy_stock_total = 0

    benefit = 0

    price_frequency = [0 for _ in range(dc[0] + 1)]
    for d in dc:
        price_frequency[d] += 1

    #print('size is :' + str(len(price_frequency)))

    #O(N) 탐색
    for stock in stocks:


        if stock != dc[current_sort_index]:
            while price_frequency[dc[current_sort_index]] <= 0:
                #print(current_sort_index)
                #이미 통과한걸로 간주
                current_sort_index += 1

            if stock != dc[current_sort_index]:
                buy_stock_num += 1
                buy_stock_total += stock
        else:


            if buy_stock_num > 0:
                benefit += stock * buy_stock_num - buy_stock_total
            buy_stock_num = 0
            buy_stock_total = 0
            current_sort_index += 1

        price_frequency[stock] -= 1

    print(benefit)
    #answer.append(benefit) # 이거 문제 아님

if __name__ == '__main__':
    #answer = []

    t = int(input())
    for _ in range(t):
        n = int(input())
        stocks = list(map(int, input().split()))

        solution(n, stocks)

    # for a in answer:
    #     print(a)

