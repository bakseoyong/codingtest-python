if __name__ == '__main__':


    tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
    for ticket in tickets:
        x, y = ticket
        print(x, y)

    tickets.sort(key= lambda x : x[1])
    print(tickets)

    str_test_1 = 'abcd'

    for s in str_test_1:
        print(s)


    str_test = ['0110', '1001', '1110']
    #for i in range(3):
        #str_test[0:2].replace('0', '1') # 'list' object has no attribute 'replace'
        #str_test[i][0] = '1' # 'str' object does not support item assignment
    real_str_list = [[] for i in range(3)]
    for index, str in enumerate(str_test):
        real_str_list[index] = list(str)

    print(str_test) # ['0110', '1001', '1110']
    print(real_str_list) # [['0', '1', '1', '0'], ['1', '0', '0', '1'], ['1', '1', '1', '0']]


    if '0' < '9':
        print('bigger than 0')

    # for index in range(0, 10):
    #     print(index)
    #     if index == 2:
    #         index += 1

    test = 0
    while test < 10:
        print(test)
        test += 1


    arr = []
    if arr:
        print(111)
    else:
        print(1000)
    print(len(arr))
    for i in range(5, 5):
        print(i) #에러없이 실행은 된다.