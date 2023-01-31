#-*- coding:utf-8 -*-
import math
import itertools

if __name__ == "__main__":
    n=int(input())
    array=list(map(int,input().split()))
    oper=list(map(int,input().split()))
    oper_set=['+','-','*','/']
    oper_list=[]

    for i in range(4):
        while oper[i]>0:
            oper[i]-=1
            oper_list.append(oper_set[i])
    oper_comb=itertools.permutations(oper_list,n-1)   
    oper_comb=list(oper_comb)  
    oper_comb=set(oper_comb) #중복제거

    min_num=999999999
    max_num=-999999999
    
    for idx,val in enumerate(oper_comb):
        value=array[0]
        for i in range(0,n-1):
            if val[i]=='+':
                value+=array[i+1]
            elif val[i]=='-':
                value-=array[i+1]  
            elif val[i]=='*':
                value*=array[i+1]  
            elif val[i]=='/':
                if(value<0):
                    value*=-1
                    value//=array[i+1]
                    value*=-1
                else:    
                    value//=array[i+1]     

        min_num=min(min_num,value)
        max_num=max(max_num,value)        

    print(max_num)
    print(min_num)    