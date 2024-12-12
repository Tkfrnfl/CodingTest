# -*- coding:utf-8 -*-
n, l = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

# 웅덩이를 시작 위치 기준으로 정렬
array.sort()

ans = 0  # 필요한 널빤지 개수
next_plank = 0  # 마지막으로 덮은 널빤지 끝 위치

for start, end in array:
    # 만약 현재 웅덩이의 시작이 이미 덮여있다면, 덮이지 않은 부분만 고려
    if start < next_plank:
        start = next_plank  # 이미 덮인 부분을 건너뛰기
    
    # 남은 구간을 널빤지로 덮어야 하는 길이
    if start < end:
        # 필요한 널빤지 개수 계산
        length_to_cover = end - start
        num_planks = (length_to_cover + l - 1) // l  # 널빤지 개수 올림 계산
        
        ans += num_planks  # 필요한 널빤지 개수 추가
        next_plank = start + num_planks * l  # 널빤지를 덮은 끝 위치 갱신

print(ans)
