dp=[[0 for col in range(101)]for row in range(101)]

def solution(m, n, puddles):
    m+=1
    n+=1
    
    puddlesCheck(puddles)

    for x in range(1,m):
        for y in range(1,n):
            if dp[x][y]!=-1:         
                #기본 초기화
                if x==1 and y==1:
                    dp[1][1]=1
                #웅덩이 카운트 제외    
                elif dp[x-1][y]==-1:
                    dp[x][y]=dp[x][y-1]
                elif dp[x][y-1]==-1:
                    dp[x][y]=dp[x-1][y]
                else:
                    dp[x][y]=dp[x-1][y]+dp[x][y-1]

    answer = dp[m-1][n-1]
    return answer%1000000007

def puddlesCheck(puddles):
    for index in puddles:
        dp[index[0]][index[1]]=-1    


if __name__ == "__main__":
	solution(4,3,[[2,2]])        