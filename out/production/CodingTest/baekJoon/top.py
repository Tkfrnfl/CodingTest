#-*- coding:utf-8 -*-
from collections import deque

if __name__ == "__main__":
    n=int(input())
    array=list(map(int, input().split()))

    ans=[0]*n       
    q=deque()

    for i in range(n):

        while q:
            stack_pop=q.pop()
            if array[i]<stack_pop[0]:
                ans[i]=stack_pop[1]
                q.append(stack_pop)     #한번이라도 걸러본적이있는 순서대로 스택됨
                break
            else:
                ans[i]=0
        q.append((array[i],i+1))

    print(*ans)


      