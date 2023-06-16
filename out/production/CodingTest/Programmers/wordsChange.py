# -*- coding: utf-8 -*- 
from copy import copy, deepcopy
from os import defpath


global mainList
global depth
global depthSave
depthSave=10000
depth=0

def solution(begin, target, words):
    

    dfs(begin,target,words,0)

    print(depthSave-1)
    if depthSave!=10000:
        answer = depthSave-1
    else:
        answer=0
    return answer

def dfs(begin,target,words,deep):

    global depthSave
    deep+=1
    nearList=[]
    # print(depth)
    print('bb:'+str(begin))
    # print('-----')
    # print(words)
    # print('\n')
    if begin==target:
        print('complet')
        if deep<depthSave:  
        # 타겟 도달시 작은 길이를 저장
            depthSave=deep
        return


    #인접 리스트 생성
    for idx,x in enumerate(words):
        diffCheck=checkNext(begin,x)

        if diffCheck==1:
            nearList.append(x)
    
    #인접 리스트 없을시
    if len(nearList)==0:
        depth=0
        return

    #인접 리스트 탐색        
    for idx,y in enumerate(nearList):
        print('b:'+str(begin))
        print('d:'+str(deep))
        print('n:'+str(nearList)) 
        tmp =deepcopy(words)
        #words.remove(y)
        tmp.remove(y)
        print('w:'+str(words))
        print('\n')
        
        dfs(y,target,tmp,deep)

# 단어가 조건에 맞는지 확인하는 함수
def checkNext(begin,targetWords): 
    diffCount=0

    for idx,x in enumerate(targetWords):
        if begin[idx] != x:
            diffCount+=1
    return diffCount        
    

if __name__ == "__main__":
	solution("hit","cog",["hot", "dot", "dog", "lot", "log"])        