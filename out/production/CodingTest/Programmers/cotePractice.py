#-*- coding:utf-8 -*-

def solution(alp, cop, problems):

    max_al=0
    max_co=0
    inf=int(1e9)

    for i in range(len(problems)):
        max_al=max(max_al,problems[i][0])
        max_co=max(max_co,problems[i][1])

    alp=min(alp,max_al)
    cop=min(cop,max_co)
    dp=[[inf]*(max_co+1)for _ in range(max_al+1)]
    dp[alp][cop]=0

    for i in range(alp,max_al+1):
        for j in range(cop,max_co+1):
            if i+1<max_al:
                dp[i+1][j]=min(dp[i+1][j],dp[i][j]+1)
            if j+1<max_co:
                dp[i][j+1]=min(dp[i][j+1],dp[i][j]+1)

            for alp_req,cop_req,alp_rwd,cop_rwd,cost in problems:
                if i>=alp_req and j>=cop_req:
                    alp_next,cop_next=min(max_al,i+alp_rwd),min(max_co,j+cop_rwd)
                    dp[alp_next][cop_next]=min(dp[i][j]+cost,dp[alp_next][cop_next])    

    answer=dp[-1][-1]
    #print(dp[-1][-1])
    return answer



if __name__ == "__main__":
    solution()