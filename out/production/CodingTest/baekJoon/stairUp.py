#-*- coding:utf-8 -*-


if __name__ == "__main__":
    n=int(input())
    array=[]
    for i in range(n):
        array.append(int(input()))

    dp=[0]*303
    dp_stack=[0]*303

    if n==1:
        print(array[0])
    if n==2:
        print(array[0]+array[1])
    if n>3:
        dp[0]=array[0]
        dp[1]=array[0]+array[1]
        dp[2]=max(array[0]+array[2],array[1]+array[2])
        for i in range(3,n):

            dp[i]= max(dp[i],(dp[i-2]+array[i]),dp[i-3]+array[i-1]+array[i])

        print(dp[n-1])    