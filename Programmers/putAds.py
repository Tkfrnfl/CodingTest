#-*- coding:utf-8 -*-
def solution(play_time, adv_time, logs):

    
    def time_exchange(time):
        hour = int(time[:2]) * 3600
        minute = int(time[3:5]) * 60
        second = int(time[6:])
    
        return hour+minute+second

    def mark_time(start,end):
        for i in range(start,end):
            time_table[i]+=1


    play_time=time_exchange(play_time)
    #mark_time(0,play_time)
    time_table=[0]*(play_time+1)

    adv_time=time_exchange(adv_time)

    for idx,val in enumerate(logs):        #log 기록
        tmp=val.split('-')
        tmp_start=time_exchange(tmp[0])
        tmp_end=time_exchange(tmp[1])
        tmp_end-=1
        # print(tmp_end)
        # print(tmp_start)
        mark_time(tmp_start,tmp_end)

    max=0
    for j in range(0,adv_time): #max init
        max+=time_table[j]

    max_mark=0
    tmp_max=max
    
    for i in range(1,play_time):        #최대값 찾기
        if adv_time+i<play_time:
            tmp_max=(tmp_max-time_table[i-1]+time_table[adv_time+i-1])
        else:
            break
        #print(max)
        if tmp_max>max:
            max=tmp_max
            max_mark=i

    #print(max_mark)       

    def get_ans(time):
        hour=time//3600
        time-=hour*3600
        min=time//60
        time-=min*60
        sec=time

        if hour<10:
            hour='0'+str(hour)
        else:
            hour=str(hour)

        if min<10:
            min='0'+str(min)
        else:
            min=str(min)

        if sec<10:
            sec='0'+str(sec)
        else:
            sec=str(sec)    

        return hour+':'+min+':'+sec
    answer = get_ans(max_mark)    
    #print(answer)
    return answer

if __name__ == "__main__":
	#solution("02:03:55","00:14:15",	["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"])   
    #solution("99:59:59","25:00:00",["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"])
    solution("50:00:00","50:00:00",["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"])