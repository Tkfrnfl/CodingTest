if __name__ == "__main__":
    n = int(input())
    now = list(input().strip())  
    aim = list(input().strip()) 

    def change(num):
        return '1' if num == '0' else '0'

    def count_flips(start_state):
        flips = 0
        if start_state != now:
            flips+=1            #첫 스위치 누르는 경우

        current_state = start_state[:]
        
        for j in range(n):
            
            if current_state != aim:
                flips += 1
                current_state[j] = change(current_state[j])
                if j==0:
                    current_state[j+1] = change(current_state[j+1])
                elif j==n-1:
                    current_state[j-1] = change(current_state[j-1])
                else:
                    current_state[j-1] = change(current_state[j-1])     
                    current_state[j+1] = change(current_state[j+1])
        
        return flips if current_state == aim else -1

    # 두 가지 경우 확인: 첫 전구를 켜고 시작 또는 끄고 시작
    result1 = count_flips(now)  
    now[0] = change(now[0]) 
    now[1] = change(now[1]) 
    result2 = count_flips(now) 

    # 결과를 출력
    if result1 == -1 and result2 == -1:
        print(-1)
    elif result1 == -1:
        print(result2)
    elif result2 == -1:
        print(result1)
    else:
        print(min(result1, result2))