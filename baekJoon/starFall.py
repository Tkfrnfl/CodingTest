if __name__ == "__main__":
    n, m, l, k = map(int, input().split())
    stars = [tuple(map(int, input().split())) for _ in range(k)]

    max_stars = 0

    # 모든 별똥별 위치를 기준으로 트램펄린을 놓아봄
    for x1, y1 in stars:
        for x2, y2 in stars:
            # 트램펄린의 왼쪽 아래 좌표를 (x1, y2)로 설정
            count = 0
            for x, y in stars:
                if x1 <= x <= x1 + l and y2 <= y <= y2 + l:
                    count += 1
            max_stars = max(max_stars, count)

    print(k - max_stars)