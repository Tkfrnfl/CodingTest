# -*- coding:utf-8 -*-
import copy

if __name__ == "__main__":
    n, m= map(int, input().split())
    arr_m = list(map(int, input().split()))
    arr_c = list(map(int, input().split()))

    ans=int(1e9)

    dp=[[0]*(sum(arr_c)+1) for _ in range(n+1)]
  

    for i in range(1,n+1):
        for j in range(sum(arr_c)+1):

            if (j<arr_c[i-1]):
                dp[i][j]= dp[i-1][j]
            else:
                dp[i][j]= max(dp[i-1][j],dp[i-1][j-arr_c[i-1]]+arr_m[i-1])    

            if dp[i][j]>=m:
                ans=min(ans,j)        

    print(ans)
    

