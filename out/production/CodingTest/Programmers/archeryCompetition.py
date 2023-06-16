#-*- coding:utf-8 -*-
from itertools import combinations

def solution(n, info):
    answer = []
    comb_list=combinations([0,1,2,3,4,5,6,7,8,9,10],n)

    for idx,val in enumerate (comb_list):
        


    return answer



if __name__ == "__main__":
    solution(5,[2,1,1,1,0,0,0,0,0,0,0])    