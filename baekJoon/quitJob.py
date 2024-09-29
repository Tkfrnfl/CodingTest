# -*- coding:utf-8 -*-
import math

if __name__ == "__main__":
    n = int(input())
    array = [list(map(int, input().split())) for _ in range(n)]

    ans =0


    def find(now, sum):
        global array
        global n
        global ans
       
        if now >= n:
            ans = max(ans, sum)
            return
        
        find(now + 1, sum)
        if now + array[now][0] <= n: 
            find(now + array[now][0], sum + array[now][1])

    find(0,0)
    print(ans)        