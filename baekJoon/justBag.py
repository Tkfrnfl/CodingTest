if __name__ == "__main__":
    n,k = map(int, input().split())
    array=[[0,0]]

    for _ in range(n):
        array.append(list(map(int, input().split())))
    
    dp =[[0]*(k+1) for _ in range(n+1)]

    ans =0

    for i in range(1,n+1):
        for j in range(1,k+1):
            w= array[i][0]
            v= array[i][1]

            if w>j:
                dp[i][j]= dp[i-1][j]
            else:
                dp[i][j]= max(dp[i-1][j],dp[i-1][j-w]+v)
                ans=max(ans, dp[i][j])

    print(ans)            