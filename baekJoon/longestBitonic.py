if __name__ == "__main__":
    n= int(input())
    array=list(map(int, input().split()))
    reArr= array[::-1]

    dp_u= [1]*n
    dp_d= [1]*n

    for i in range(1,n):
        for j in range(i):
            if array[i]>array[j]:
                dp_u[i]=max(dp_u[i],dp_u[j]+1)

            if reArr[i]>reArr[j]:
                dp_d[i]=max(dp_d[i],dp_d[j]+1) 

    dp_d=dp_d[::-1]
    ans =0

    for i in range(n):
        ans =max(ans,dp_u[i]+dp_d[i])

    print(ans-1)    