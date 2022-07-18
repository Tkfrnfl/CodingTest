global mainList


def solution(begin, target, words):

    global mainList
    mainList=words.copy()

    dfs(begin)

    answer = 0
    return answer

def dfs(begin):
    global mainList

    for idx,x in enumerate(mainList):
        checkDiff=checkNext(begin,x)
        if checkDiff==1:
            del mainList[idx] # 한글자만 틀릴시 메인리스트에서 삭제
            

# 단어가 조건에 맞는지 확인하는 함수
def checkNext(begin,targetWords): 
    diffCount=0

    for idx,x in enumerate(targetWords):
        if begin[idx] != x:
            diffCount+=1
    return diffCount        
    

if __name__ == "__main__":
	solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"])        