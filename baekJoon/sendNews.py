if __name__ == "__main__":
    n= int(input())
    arr=list(map(int, input().split())) 


    dp=[0]*n

    # 각 직원별 부하 리스트
    sub_list=[[]for _ in range(n)]

    for i in range(1,n):
        sub_list[arr[i]].append(i)

    mx =0
    for sub in sub_list:
        if len(sub)>0:
            sub_order_list =[] # 뉴스 전할 부하를 부하의 부하 많은 순으로 고르기
            for i in sub:
                sub_order_list.append((i,len(sub_list[i])))
            sub_order_list.sort(key=lambda x:x[1] ,reverse=True)       

            sub_idx=1
            for sub_or in sub_order_list:
                dp[sub_or[0]]=dp[arr[sub_or[0]]]+sub_idx
                sub_idx+=1
                mx = max(mx,dp[sub_or[0]]) #이미 그리디로 최소값을 찾은 상태기에 모두 순회했다는 의미의 max값 탐색

    print(mx)

    
    


