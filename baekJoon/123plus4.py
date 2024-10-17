if __name__ == "__main__":
    
    t = int(input())
    array = [int(input()) for _ in range(t)]
    
    max_n = max(array)  
    

    dp = [0] * (max_n + 2)
    dp[0] = 1  
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    dp[4] = 4
    def max3(num):
        m3=0
        cnt=1
        if num%3 ==1:
            m3 =(num//3)-1
        # if num%3 ==0:
        #     cnt+=1
        #     m3 =(num//3)
        else:
            m3 =(num//3) 

        while m3>=2:
            m3-=2
            cnt+=1

        return cnt    

    for i in range(5, max_n +1):
        dp[i] = dp[i - 1]+ max3(i)
    
    # print(dp)
    for value in array:
        print(dp[value])