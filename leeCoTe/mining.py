#-*- coding:utf-8 -*-
def solution():
    array1=[[1,3,3,2],[2,1,4,1],[0,6,4,7]]
    array2=[[1,3,1,5],[2,2,4,1],[5,0,2,3],[0,6,1,2]]

    dp=[[0 for j in range(10)]for i in range(10)]

    #1번 테스트 케이스
    for i in range(0,4):
        for j in range(0,3):
            up=0
            mid=0
            down=0
            if i==0:
                dp[i][j]=array1[j][i]
            else:
                if j-1>=0:
                    up=dp[i-1][j-1]
                if dp[i-1][j] is not None:
                    mid=dp[i-1][j]
                if j+1 <3:
                    down=dp[i-1][j+1]       

                dp[i][j]=max(up+array1[j][i],mid+array1[j][i],down+array1[j][i])  

    dp=[[0 for j in range(10)]for i in range(10)]              
    #2번 테스트 케이스
    for i in range(0,4):
        for j in range(0,4):
            up=0
            mid=0
            down=0
            if i==0:
                dp[i][j]=array2[j][i]
            else:
                if j-1>=0:
                    up=dp[i-1][j-1]
                if dp[i-1][j] is not None:
                    mid=dp[i-1][j]
                if j+1 <4:
                    down=dp[i-1][j+1]       

                dp[i][j]=max(up+array2[j][i],mid+array2[j][i],down+array2[j][i])
        print(dp)          
if __name__ == "__main__":
	solution()      