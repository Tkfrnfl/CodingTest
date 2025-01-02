if __name__ == "__main__":
    n = int(input())
    array = list(map(int, input().split()))

    mx = 0

    for i in range(n):
        cnt_l = 0
        cnt_r = 0

        # 왼쪽
        arr_l = array[:i]
        prev_val = None
        prev_idx = -1
        for idx, val in enumerate(arr_l[::-1]):  # 역순 순회
            if prev_val is None or (array[i] - val) * (prev_idx + 1) >= (array[i] - prev_val) * (idx + 1):
                prev_val = val
                prev_idx = idx
                cnt_l += 1

        # 오른쪽
        arr_r = array[i + 1:]
        prev_val = None
        prev_idx = -1
        for idx, val in enumerate(arr_r):  # 정순 순회
            if prev_val is None or (array[i] - val) * (prev_idx + 1) >= (array[i] - prev_val) * (idx + 1):
                prev_val = val
                prev_idx = idx
                cnt_r += 1

        # 결과 계산
        mx = max(mx, cnt_l + cnt_r)

    print(mx)
