def solution(gems):
    answer_length = 1000000
    answer = []
    front = end = 0

    total = len(set(gems))
    print(total)

    # d = {item : 0 for item in set(gems)}
    # print(d)

    temp = {}

    while end < len(gems):
        if gems[end] not in temp:
            temp[gems[end]] = end

        if len(temp) == total:
            # 구간 줄여보기
            for i in range(front, end + 1):
                temp[gems[i]] = i

            # 정렬해서 첫, 마지막 가져와서 +1씩해서 저장
            sortedTemp = sorted(temp.values())
            first, last = sortedTemp[0], sortedTemp[-1]

            # 정답 갱신
            if answer_length > last - first:
                answer_length = last - first
                answer = []
                answer.append(first + 1)
                answer.append(last + 1)
                print(answer)

            del temp[gems[first]]
            front = first

        end += 1

    return answer