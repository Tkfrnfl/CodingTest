def solution(numbers):
    mutNumber=[]

    for x in numbers:
        tmp=(str(x)*4)[:4] #4자릿수까지 반복시킨다음에 비교,
        length=len(str(x)) #원래수의 크기 저장
        mutNumber.append((tmp,length))  
    mutNumber.sort(reverse=True)
  
    answer=''
    for y in mutNumber:
        answer=answer+y[0][:y[1]]
    return str(int(answer))


if __name__ == "__main__":
	solution([70,0,0,0,0])     