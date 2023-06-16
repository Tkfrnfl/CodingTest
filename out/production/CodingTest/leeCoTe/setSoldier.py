#-*- coding:utf-8 -*-
def solution():
    array=[15,11,4,8,5,2,4]

    dp=[0]*100
    dp[0]=1

    for i in range(1,len(array)):
        for j in range(0,i):
            if array[i]<array[j]:
                dp[i]=dp[j]+1
    print(dp)
if __name__ == "__main__":
	solution()    