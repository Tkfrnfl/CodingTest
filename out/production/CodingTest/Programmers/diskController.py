


def solution(jobs):

    jobs.sort(key=lambda x:(x[0],x[1]))    
    print(jobs)
    time=[]
    workQueue=[]

    workQueue.append(jobs[0])
    total=jobs[0][0]
    jobs.remove(jobs[0])

    
    while(len(workQueue)!=0):

        if len(workQueue)==1: # 큐에 하나남을시

            time.append(total-workQueue[0][0]+workQueue[0][1])
            total=total+workQueue[0][1]

            workQueue.remove(workQueue[0])


            if(len(jobs)>0 and total<jobs[0][0]):  # 아직 시간 안됬을때 남은 일 확인
                total=jobs[0][0]
                workQueue.append(jobs[0]) #큐에 추가
                jobs.remove(jobs[0])

            if(len(jobs)>0 and total>=jobs[0][0]):# 시간 됬을때 남은 일 확인
                while(len(jobs)>0 and total>=jobs[0][0]):
                    workQueue.append(jobs[0]) #큐에 추가
                    jobs.remove(jobs[0])
                print(workQueue)
                print(total)    
            continue            

        elif len(workQueue)>1: # 2개 이상일시 가장 작은것 선택
            workQueue.sort(key=lambda  x:(x[1],x[0]))
            time.append(total-workQueue[0][0]+workQueue[0][1])
            total=total+workQueue[0][1]
            workQueue.remove(workQueue[0])

            if(len(jobs)>0 and total<jobs[0][0]):  # 아직 시간 안됬을때 남은 일 확인
                total=jobs[0][0]
                workQueue.append(jobs[0]) #큐에 추가
                jobs.remove(jobs[0])
            if(len(jobs)>0 and total>=jobs[0][0]):# 시간 됬을때 남은 일 확인
                while(len(jobs)>0 and total>=jobs[0][0]):
                    workQueue.append(jobs[0]) #큐에 추가
                    jobs.remove(jobs[0])
    answer = 0
    for x in time:
        answer+=x
    answer= answer/len(time)
    print(int(answer))
    return answer


if __name__ == "__main__":
	solution([[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]])      


# 문제에선 들어오는 job의 우선순위를 미리 다 계산하고 풀어야함,
# 내가푼것은 들어오는job을 모른다는 가정에서 가능한 코드.
#     *하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리합니다. <-오류 유발 문제 지문