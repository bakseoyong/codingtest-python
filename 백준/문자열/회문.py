def solve():
    n = int(input())

    strs = []
    for i in range(n):
        strs.append(input())

    for str in strs:
        left = 0
        right = len(str) - 1
        while left < right:
            if str[left] == str[right]:
                left += 1
                right -= 1
            else:
                if left <= right - 1:
                    temp = str[:right] + str[right+1:]
                    if temp[:] == temp[::-1]:
                        print(1)
                        break
                if left + 1 < right:
                    temp = str[:left] + str[left+1:]
                    if temp[:] == temp[::-1]:
                        print(1)
                        break
                print(2)
                break
        if left >= right:
            if str[:] == str[::-1]:
                print(0)
            else:
                print(2)


if __name__ == '__main__':
    solve()