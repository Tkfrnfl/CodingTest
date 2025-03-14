#-*- coding:utf-8 -*-


if __name__ == "__main__":
    n=int(input())
    array=[]
    for i in range(n):
        array.append(int(input()))

    dp=[0]*303
    
    dp[0]=0
    dp[1]=array[0]


    if n==1:
        print(dp[1])
    else:    
        dp[2]=array[0]+array[1]
        for i in range(3,n+1):
            dp[i]=max(dp[i-3]+array[i-2]+array[i-1],dp[i-2]+array[i-1])

        print(dp[n])    