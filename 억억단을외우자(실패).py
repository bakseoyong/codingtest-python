import math

for문 두개써서 이용하면
i, j 두개로 for문 돌리고
곱한 값이 e 이상이면 컷

곱하면서 제곱근 인지 확인하면 1만더하고
제곱근이 아니라면 +2를 하는데 이러

i , j 가 2, 1이고 1, 2이면 ?

result

def solution(e, starts):
    answer = []

    most_frequency_nums = []
    most_frequency_nums_size = 0

    for index in range(1, e + 1):
        nums = 0

        sqrt = int(math.sqrt(index))
        for i in range(1, sqrt + 1):
            if index % i == 0:
                nums += 2
                #제곱근이라면
                if i == index / i:
                    nums -= 1

        if nums == most_frequency_nums_size:
            most_frequency_nums.append(index)
        if most_frequency_nums_size < nums:
            most_frequency_nums = [index]
            most_frequency_nums_size = nums

        #print(most_frequency_nums)

    for start in starts:
        for most_frequency_num in most_frequency_nums:
            if most_frequency_num > start:
                answer.append(most_frequency_num)
                break

    #print(answer)
    return answer

if __name__ == '__main__':
    e = 8
    starts = [1, 3, 7]

    solution(e, starts)
