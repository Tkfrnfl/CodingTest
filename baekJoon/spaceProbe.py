def floyd_warshall(n, array):
    # 플로이드-워셜 초기화
    for k in range(n):
        for i in range(n):
            for j in range(n):
                array[i][j] = min(array[i][j], array[i][k] + array[k][j])

def calculate_minimum_exploration_time(n, start, array):
    floyd_warshall(n, array)

    min_exploration_time = float('inf')
    for i in range(n):
        if i != start:
            min_exploration_time = min(min_exploration_time, array[start][i])

    return min_exploration_time

# 입력 받기
if __name__ == "__main__":
    n, k = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(n)]

    # 모든 행성을 탐사하는 최소 시간을 계산하고 결과 출력
    result = calculate_minimum_exploration_time(n, k, array)
    print(result)
