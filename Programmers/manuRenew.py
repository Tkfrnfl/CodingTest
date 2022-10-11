#-*- coding:utf-8 -*-
from itertools import combinations, permutations

def solution(orders, course):
    answer = []
    sum_list=[]
    ans_list=[]
    ans_max_list=[0 for i in range(100)]
    ans_max_word=[[0]*100 for _ in range(100)]

    def get_combi(order_list,num):
        sub_list=str(order_list)
        tmp_list=list(permutations(sub_list,num))

        for idx,val in enumerate(tmp_list):
            if val in sum_list:
                ans_list.append(val)    #2번이상 나오는조합
            else :
                sum_list.append(val)    #한번만 나오는조합
    for idx,val in enumerate(orders):
        for id,va_num in enumerate(course):
            get_combi(val,va_num)
    
    for id,va_num in enumerate(course):
        for idx,val in enumerate(ans_list):
            if len(val)==va_num:
                if ans_list.count(val)>ans_max_list[id]:
                    ans_max_list[id]= ans_list.count(val) #최대값 저장
                    ans_max_word[id]=[]
                    ans_max_word[id].append(val)          #최대값 단어 저장
                elif ans_list.count(val)==ans_max_list[id]:     #같은경우 따로 저장
                    ans_max_word[id].append(val)          #기존에 이어붙이기


    for idx,val in enumerate(course):                      
        ans_max_word[idx]=list(set(ans_max_word[idx]))      #중복제거
        
        for idx_sub,val_sub in enumerate(ans_max_word[idx]):
            tmp=''

            if type(val_sub) is tuple:
                for id,va_num in enumerate(val_sub):    
                    tmp +=va_num
                answer.append(tmp)

    #print(ans_max_word[0])
    for idx,val in enumerate(answer):
        answer[idx]="".join(sorted(val))  #중복제거

    answer=list(set(answer))
    answer.sort()
    #print(answer)
    return answer

if __name__ == "__main__":
	solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5])         