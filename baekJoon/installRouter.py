#-*- coding:utf-8 -*-
def search(num, array, c, n):
    now = array[0]
    count = 1  # 첫 번째 공유기는 설치한 것으로 간주
    for i in range(1, n):
        if array[i] >= now + num:  # 거리가 num 이상이면 설치
            count += 1
            now = array[i]  # 현재 위치 갱신
            if count >= c:  
                return True
    return False

if __name__ == "__main__":
    n, c = map(int, input().split())
    array = [int(input()) for _ in range(n)]
    array.sort()

    start = 1  
    end = array[-1] - array[0]  
    ans = 0

    while start <= end:
        mid = (start + end) // 2
        if search(mid, array, c, n):
            ans = mid  # 가능한 거리이므로 저장
            start = mid + 1  # 더 큰 거리 탐색
        else:
            end = mid - 1  # 더 작은 거리 탐색

    print(ans)
