# -*- coding:utf-8 -*-
from collections import deque
from itertools import combinations

if __name__ == "__main__":
    l,c = map(int, input().split())
    array = list(map(str, input().split()))

    array.sort()

    vowel=[ord('a'),ord('e'),ord('i'),ord('o'),ord('u')]

    ans_list=[]

    comb = list(combinations(range(c),l))

    for com in comb:
        list(com).sort()

        vowel_num=0
        cons_num =0
        for c in com:
            if ord(array[c]) in vowel:
                vowel_num+=1
            else:
                cons_num+=1

        string=''
        if vowel_num>0 and cons_num>1:
            for c in com:
                string+= str(array[c])

            ans_list.append(string)

    for lis in ans_list:
        print(lis)       
        