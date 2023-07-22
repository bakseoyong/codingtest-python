import copy


def recursive(arr, m):
    if len(arr) == m:
        operators.append(copy.deepcopy(arr))
        return

    arr.append(' ')
    recursive(arr, m)
    arr.pop()

    arr.append('+')
    recursive(arr, m)
    arr.pop()

    arr.append('-')
    recursive(arr, m)
    arr.pop()


n = int(input())

for _ in range(n):
    operators = []
    m = int(input())
    recursive([], m - 1)
    # print(operators)

    for operator in operators:
        statement = ''
        for i in range(m - 1):
            statement += str(i + 1) + operator[i]
        statement += str(m)
        if (eval(statement.replace(' ', ''))) == 0:
            print(statement)
    print()
