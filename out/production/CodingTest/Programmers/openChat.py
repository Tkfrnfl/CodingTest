# -*- coding: utf-8 -*-

from copy import deepcopy


def solution(record):
    dict={}          #Make hash dictionary 
    answer=[]
    for x in record:
        tmp=x.split()
        
        if tmp[0]=="Enter":    
            dict[tmp[1]]=tmp[2]  #Save hash dictionary 
            answer.append(tmp[1]+"님이 들어왔습니다.")
        elif tmp[0]=="Leave":
            answer.append(tmp[1]+"님이 나갔습니다.")
        elif tmp[0]=="Change":
            dict[tmp[1]]=tmp[2]

    for idx,y in enumerate(answer):  #Match hash value 
        y=y.split('님')
        answer[idx]=dict[y[0]]+'님'+y[1]
            
    return answer

if __name__ == "__main__":
	solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])  