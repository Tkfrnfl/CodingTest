import copy
from collections import deque
from itertools import permutations

if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    
    order =[1,2,3,4,5,6,7,8]
    tmp_arr = copy.deepcopy(arr)
    tmp_arr[0][0]= -1
    mx= 0

    for perm in permutations(order):
        o_list = list(perm[:3])+[0]+list(perm[3:])

        ans=0

        idx =0
        
        for i in arr:
            o_cnt=0
            queue = deque()

            while True:
                score= i[o_list[idx%9]]

                if score ==0:
                    o_cnt+=1
                else:
                    queue.append(1)  
                    for _ in range(score-1):
                        queue.append(0)  
                if o_cnt>2:
                    idx+=1
                    break

                while len(queue) >3:
                    pop= queue.popleft()

                    if pop==1:
                        ans+=1

                idx+=1
        mx =max(mx,ans)        

    print(mx)

