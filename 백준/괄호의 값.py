def stack_calculator():
    temp = []

    # *가 나올때 까지 계산해주면 된다.
    while True:

        if len(operator_stack) == 0:
            return temp.pop()

        p = operator_stack.pop()

        if p == '*':
            # 종료 조건
            operator_stack.append('*')
            return temp.pop()

        elif p != '+':
            temp.append(p)
            continue
        elif p == '+':
            another = operator_stack.pop()
            a = temp.pop()
            temp.append(a + another)






if __name__ == '__main__':
    str = input()

    str_stack = []
    operator_stack = []
    answer = 0

    for index in range(len(str)):

        if index == 0:
            if str[index] == ')' or str[index] == ']':
                answer = 0
                break
            str_stack.append(str[index])
            continue

        if str[index] == '(' or str[index] == '[':
            str_stack.append(str[index])

            if str[index - 1] == '(' or str[index - 1] == '[':
                operator_stack.append('*')
                # if str[index - 1] == '(':
                #     operator_stack.append(2)
                # elif str[index - 1] == '(':
                #     operator_stack.append(3)

                # 위의 4줄도 닫고, 닫고 가 되면 그때 2 냐 3 이냐를 따지면 됨
            elif str[index - 1] == ')' or str[index - 1] == ']':
                operator_stack.append('+')
                # 2냐 3이냐는 ) or } 이 나왔을 때 했었을 것이므로

        elif str[index] == ')':
            # 괄호가 닫히면 일단 예외조건만 확인하고
            # 바로 stack_calculator 돌려서 연산자 스택 정리해준다.(여기서 정리해야 하는 이유 : () {} )
            # 나온 값이 있는데 만약 전 인덱스 값이 닫히는 문자였다면 거기에 곱하기 하면 된다.
            # 어디까지 곱하냐 : 처음에 '*' 문자를 넣었을 때 까지
            if str[index - 1] == '[':
                answer = 0
                break
            elif str[index - 1] == '(':
                str_stack.pop()
                operator_stack.append(2)

                temp = stack_calculator()
                operator_stack.append(temp)
                answer = operator_stack[0]



            if str[index - 1] == ')' or str[index - 1] == ']':
                # 정리된 값 리턴
                if len(str_stack) == 0:
                    answer = 0
                    break
                temp = stack_calculator()
                operator_stack.append(temp)
                answer = operator_stack[0]

                # ------------------

                temp = operator_stack.pop()
                #calculator에서 * 일경우 다시 넣었으니 그 연산자를 제거해줘야 한다.
                trash = operator_stack.pop()
                operator_stack.append(temp * 2)
                answer = operator_stack[0]
        elif str[index] == ']':
            if str[index - 1] == '(':
                answer = 0
                break
            elif str[index - 1] == '[':
                str_stack.pop()
                operator_stack.append(3)

                temp = stack_calculator()
                operator_stack.append(temp)
                answer = operator_stack[0]


            if str[index - 1] == ')' or str[index - 1] == ']':
                if len(str_stack) == 0:
                    answer = 0
                    break
                temp = stack_calculator()
                operator_stack.append(temp)
                answer = operator_stack[0]

            # ( () {} ) 이면 내 안에 있는 () {} 계산해주고 *2 해야된다.
            # 다시 뻇다가 넣는 이유 : str[index - 1] == '(' 때문에
                temp = operator_stack.pop()
                # calculator에서 * 일경우 다시 넣었으니 그 연산자를 제거해줘야 한다.
                trash = operator_stack.pop()
                operator_stack.append(temp * 3)
                answer = operator_stack[0]

    if answer != 0:
        answer = stack_calculator()
    print(answer)

