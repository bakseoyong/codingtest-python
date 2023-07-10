import math

def solution(alp, cop, problems):
    answer = 0

    require_alp = 0
    require_cop = 0

    #목표로 하는 코딩력, 알고력 계산하기
    for problem in problems:
        require_alp = max(problem[0], require_alp)
        require_cop = max(problem[1], require_cop)

    #dp 크기 설정은 alp, cop min 설정 이전에 해도 상관없다. 이전, 이후 상관없이 할당되는 크기는 같기 때문
    dp = [[math.inf for _ in range(alp, require_cop + 1)] for _ in range(cop, require_cop + 1)]

    #현재의 코딩력과 알고력이 높아 처음부터 모든 문제를 풀 수 있는 가능성이 있다.
    alp = min(alp, require_alp)
    cop = min(cop, require_cop)

    dp[alp][cop] = 0

    #목표치를 계산했으니까 다음은 여기에 다가가기
    #dp사용
    for i in range(alp, require_alp + 1):
        for j in range(cop, require_cop + 1):
            if i < require_alp: # i + 1을 해 줄건더ㅔ require_alp == i 이면 인덱스를 벗어난다.
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
            if j < require_cop:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)

            #문제풀기
            for problem in problems:
                # 요구하는 코딩력와 알고력을 i,j가 넘으면 i + 요구코딩력, j + 요구알고력 인덱스에 그만큼 시간을 단축시킬 수 있는 가능성이 있다.
                # 문제를 풀다보면 require_alp와 require_cop를 넘을 수 있는데 이것도 전부 require alp, cop 안에 집어넣는다.
                if i >= problem[0] and j >= problem[1]:

                    after_alp = i + problem[2]
                    after_cop = j + problem[3]

                    if after_alp >= require_alp and after_cop >= require_cop:
                        after_alp = require_alp
                        after_cop = require_cop
                    #위의 다섯줄을 min으로 하면 min(i + problem[2] , require_alp) * 2 = 2줄로 간단하게 표현할 수 있다.


                    # 문제 풀기 가능
                    dp[after_alp][after_cop] = min(dp[after_alp][after_cop], dp[i][j] + problem[4])

    answer = dp[after_alp][after_cop]
    return answer

if __name__ == '__main__':
    alp = 10
    cop = 10
    problems = [[10,15,2,1,2],[20,20,3,3,4]]

    solution(alp, cop, problems)

