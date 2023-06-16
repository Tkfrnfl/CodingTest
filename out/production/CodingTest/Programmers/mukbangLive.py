#-*- coding:utf-8 -*-

def sol(list,k):
    #최소값구하기
    min_num=int(1e9)
    for i in range(len(list)):
        if list[i]!=0:
            min_num=min(min_num,list[i])
    
    quotient=min(k//len(list),min_num)

    if k//len(list) <(min_num-1):
        return k%len(list)
    else:    
        k-=(quotient*len(list)) 
        len_list=len(list)
        for i in range(len_list):
            list[i]-=quotient

        return sol(list,k)        


def solution(food_times, k):

    answer = sol(food_times,k)

    print(answer)
    return answer



if __name__ == "__main__":
    solution([3, 1, 2],5)
    #solution([8, 9, 2,9,9],20)