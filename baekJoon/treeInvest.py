if __name__ == "__main__":
    n, m, k = map(int, input().split())
    arr_a = [list(map(int, input().split())) for _ in range(n)]
    arr_t = [list(map(int, input().split())) for _ in range(m)]

    ans = 0

    # Initialize
    tree_list = [[[] for _ in range(n)] for _ in range(n)]
    nutri_list = [[5] * n for _ in range(n)]

    for x, y, age in arr_t:
        tree_list[x - 1][y - 1].append(age)

    for year in range(k):
        # Spring
        for j in range(n):
            for i in range(n):
                # Sort trees by age to process younger trees first
                tree_list[j][i].sort()
                alive_trees = []
                dead_trees = 0

                for age in tree_list[j][i]:
                    if nutri_list[j][i] >= age:
                        nutri_list[j][i] -= age
                        alive_trees.append(age + 1)
                    else:
                        dead_trees += age // 2

                # Update the list with alive trees only
                tree_list[j][i] = alive_trees
                nutri_list[j][i] += dead_trees  # Add nutrients from dead trees # summer

        # Fall
        grow_list = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for j in range(n):
            for i in range(n):
                for age in tree_list[j][i]:
                    if age % 5 == 0:  
                        for dj, di in grow_list:
                            nj, ni = j + dj, i + di
                            if 0 <= nj < n and 0 <= ni < n:
                                tree_list[nj][ni].append(1)

        # Winter
        for j in range(n):
            for i in range(n):
                nutri_list[j][i] += arr_a[j][i]

    # Count the remaining trees
    ans = sum(len(trees) for row in tree_list for trees in row)
    print(ans)
