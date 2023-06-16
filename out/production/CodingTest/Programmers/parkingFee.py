#-*- coding:utf-8 -*-
import math

def solution(fees, records):

    basic_min=fees[0]
    basic_fee=fees[1]
    unit_min=fees[2]
    unit_fee=fees[3]

    car_num=[0]*9999

    def fee_calc(val):
        if val<basic_min:
                return basic_fee
        else:
            return (basic_fee+math.ceil(float(val-basic_min)/float(unit_min))*unit_fee)    

    # 각 번호별로 출입 시간만 리스트화 하여 저장
    for idx,val in enumerate(records):
        tmp_time=val.split(' ')[0]
        hour=int(tmp_time.split(':')[0])
        min=int(tmp_time.split(':')[1])
        total_time=hour*60+min
        car=int(val.split(' ')[1])

        tmp_list=[]
        if type(car_num[car])is int:
            tmp_list.append(total_time)
            car_num[car]=tmp_list
        else:
            for idy,valy in enumerate(car_num[car]):
                tmp_list.append(valy)
            tmp_list.append(total_time)
            car_num[car]=tmp_list

    answer = []        


    # in,out 홀짝 별로 나누어 계산
    for idx,val in enumerate(car_num):
        if val!=0:
            time_sum=0
            for i in range(0,((len(val)//2)+1)):
                
                if len(val)==(i*2):
                    continue
                if len(val)==((i*2)+1):       #마지막에 out 없는 경우
                    time_sum+=(1439-val[i*2])
                else:   
                    time_sum+=(val[(i*2)+1]-val[i*2])
            answer.append(fee_calc(time_sum))    

     
  
    return answer

if __name__ == "__main__":
	solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])     