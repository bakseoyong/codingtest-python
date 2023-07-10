def solution(jobs):
    answer = 0

    jobs.sort(key=lambda x: x[0])

    # 순회를 돌면서 time 보다 작은 것들중에 고른다.
    # time 보다 크면 거기서 인덱스 종료
    # time 갱신되면 다시 저장

    time = 0
    current_waiting_index = 0

    finished = [False for _ in range(len(jobs))]
    finish_time = [0 for _ in range(len(jobs))]
    hrn = [0.0 for _ in range(len(jobs))]
    remain_jobs = len(jobs)

    while remain_jobs > 0:
        for index in range(current_waiting_index, len(jobs)):
            if jobs[index][0] > time:
                current_waiting_index = index - 1 # 이번 인덱스 -1 까지 가능하다.
                break

        min_time

        for i in range(current_waiting_index + 1):
            if not finished[i]:
                waiting_time = time - jobs[i][0]
                service_time = jobs[i][1] - jobs[i][0]

                hrn[i] = (waiting_time + service_time) / service_time


                finished[i] = True
                remain_jobs -= 1
                time += service_time
                finish_time[i] = time

    return answer

if __name__ == '__main__':
    jobs = [[0, 3], [1, 9], [2, 6]]

    solution(jobs)

    # 우선순위 큐 사용하면 될 것 같다.

    # HRN 비선점형 스케줄링을 구현해서 테스트
    # HRN의 우선순위 공식 : (대기시간 + 서비스시간) / 서비스시간 이다.

    #하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리합니다.