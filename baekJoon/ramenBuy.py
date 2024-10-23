# # -*- coding:utf-8 -*-
  
if __name__ == "__main__":
    n = int(input())
    array = list(map(int, input().split()))

    cost = 0

    # 먼저 3개씩 살 수 있는 구간은 최대한 산다
    for i in range(n - 2):
        if array[i + 1] > array[i + 2]:  # 중간 구간 조정
            buy = min(array[i], array[i + 1] - array[i + 2])
            array[i] -= buy
            array[i + 1] -= buy
            cost += 5 * buy
        
        buy = min(array[i], array[i + 1], array[i + 2])
        array[i] -= buy
        array[i + 1] -= buy
        array[i + 2] -= buy
        cost += 7 * buy

    # 2개씩 살 수 있는 구간 처리
    for i in range(n - 1):
        buy = min(array[i], array[i + 1])
        array[i] -= buy
        array[i + 1] -= buy
        cost += 5 * buy

    # 남은 라면은 1개씩 구매

    cost += 3 * sum(array)

    print(cost)
