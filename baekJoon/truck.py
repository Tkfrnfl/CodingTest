#-*- coding:utf-8 -*-

from collections import deque

if __name__ == "__main__":
    n, l, w = map(int, input().split())  
    array = list(map(int, input().split()))  

    q = deque([0] * l) 
    sm = 0  
    time = 0  

    for a in array:
        while True:
            time += 1
            pop = q.popleft() 
            sm -= pop

            if sm + a <= w:  # 새로운 트럭이 올라갈 수 있는지 확인
                q.append(a)  # 트럭이 다리에 올라감
                sm += a
                break
            else:
                q.append(0)  # 트럭이 올라가지 못하면 빈 공간만 추가

    time += l

    print(time)


