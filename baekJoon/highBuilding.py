if __name__ == "__main__":
    n = int(input())
    array = list(map(int, input().split()))


    mx = 0

    for i in range(n):
        cnt_l = 0
        cnt_r = 0
        # i기준 왼쪽
        arr_l = array[:i]
        prev_val = int(1e9)
        prev_idx = 0
        bigger_l = False
        bigger_r = False
        for idx, val in enumerate(arr_l[::-1]):
            if bigger_l:        
                # 기울기를 정수 비교로 변경
                if (array[i] - val) * (prev_idx + 1) < (array[i] - prev_val) * (idx + 1):
                    prev_val = val
                    prev_idx = idx
                    cnt_l += 1
            else:    
                if (array[i] - val) * (prev_idx + 1) >= (array[i] - prev_val) * (idx + 1):
                    prev_val = val
                    prev_idx = idx
                    cnt_l += 1
            if val> array[i]:
                bigger_l =True        

        if len(arr_l) > 0 and cnt_l == 0:
            cnt_l += 1
        # i기준 오른쪽
        arr_r = array[i + 1:]
        prev_val = int(1e9)
        prev_idx = 0
        for idx, val in enumerate(arr_r):
            if bigger_r:
                # 기울기를 정수 비교로 변경
                if (array[i] - val) * (prev_idx + 1) < (array[i] - prev_val) * (idx + 1):
                    prev_val = val
                    prev_idx = idx
                    cnt_r += 1
            else:    
                # 기울기를 정수 비교로 변경
                if (array[i] - val) * (prev_idx + 1) >= (array[i] - prev_val) * (idx + 1):
                    prev_val = val
                    prev_idx = idx
                    cnt_r += 1

            if val> array[i]:
                bigger_r =True           

        if len(arr_r) > 0 and cnt_r == 0:
            cnt_r += 1

        mx = max(mx, cnt_l + cnt_r)

    print(mx)
