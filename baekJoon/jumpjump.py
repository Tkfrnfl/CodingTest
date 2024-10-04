if __name__ == "__main__":
    n= int(input())
    arr=list(map(int, input().split())) 

    INF = int(1e9)
    dp=[INF]*n

    ans =0
    dp[0]=0
        

    for i in range(n):
        for j in range(i):
            if arr[j]+j>=i:
                dp[i]= min(dp[i],dp[j]+1)

    if dp[n-1]== INF:
        ans =-1
    else:
        ans= dp[n-1]

    if arr[0]==0:
        ans= -1  
    if n==1:
        ans=0

    print(ans)            
    