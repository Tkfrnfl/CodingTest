#-*- coding:utf-8 -*-


if __name__ == "__main__":
    n=int(input())
    array=[]

    for i in range(n):
        tmp=list(map(int,input().split()))
        array.append(tmp)
        
    dp=[[0 for _ in range(3)]for _ in range(2) ]
    #초기화
    dp[0][0]= [array[0][0],array[0][0]]
    dp[0][1]=[array[0][1],array[0][1]]
    dp[0][2]=[array[0][2],array[0][2]]

    if n==1:                    #n=1 고려
        print(max(array[0]),min(array[0]))

    if n>1:    

        for i in range(1,n):
            a=max(max(dp[0][0]),max(dp[0][1]))+array[i][0]
            b=min(min(dp[0][0]),min(dp[0][1]))+array[i][0]
            dp[1][0]=[a,b]
            a=max(max(dp[0][0]),max(dp[0][1]),max(dp[0][2]))+array[i][1]
            b=min(min(dp[0][0]),min(dp[0][1]),min(dp[0][2]))+array[i][1]
            dp[1][1]=[a,b]
            a=max(max(dp[0][1]),max(dp[0][2]))+array[i][2]
            b=min(min(dp[0][1]),min(dp[0][2]))+array[i][2]
            dp[1][2]=[a,b]

            dp[0][0]=dp[1][0]
            dp[0][1]=dp[1][1]
            dp[0][2]=dp[1][2]
            
        print(max(max(dp[1][0]),max(dp[1][1]),max(dp[1][2])),min(min(dp[1][0]),min(dp[1][1]),min(dp[1][2])))



