import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    array = [list(map(int, input().split())) + [i] for i in range(n)]  # (색, 크기, 원래 인덱스) 저장

    # 크기 기준 정렬 (같은 크기면 원래 입력 순서 유지)
    array.sort(key=lambda x: x[1])

    total_sum = 0  # 전체 공들의 크기 합
    color_sum = {}  # 색상별 크기 합
    answer = [0] * n  # 결과 저장용

    j = 0
    for i in range(n):
        color, size, idx = array[i]

        # 크기가 작은 공들 합산 (현재 공보다 작은 크기만 포함)
        while j < i and array[j][1] < size:
            total_sum += array[j][1]
            color_sum[array[j][0]] = color_sum.get(array[j][0], 0) + array[j][1]
            j += 1
        # 현재 공이 잡을 수 있는 크기 합 = 전체 누적합 - 같은 색상의 크기 합
        answer[idx] = total_sum - color_sum.get(color, 0)

    # 결과 출력
    sys.stdout.write("\n".join(map(str, answer)) + "\n")
