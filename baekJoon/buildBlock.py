# -*- coding:utf-8 -*-

if __name__ == "__main__":
    n, m, h = map(int, input().split())
    array=[]
    for _ in range(n):
        a= list(map(int, input().split()))
        array.append(a)

    dp=[[0]*(h+1) for _ in range(n+1)]

    # 초기값 설정
    for i in range(1,n+1):
        for a in array[i-1]:
            dp[i][a]+=1

    for i in range(1,n+1):
        for j in range(h+1):
            dp[i][j]+=dp[i-1][j]

            for a in array[i-1]:
                if j-a>0:
                    dp[i][j]+=dp[i-1][j-a] 
    sum=0

    print(dp[n][h]%10007)                
            

    