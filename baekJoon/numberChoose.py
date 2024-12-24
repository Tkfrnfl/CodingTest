from collections import defaultdict

def find_cycles(n, second_row):
    graph = defaultdict(int)
    for i in range(n):
        graph[i + 1] = second_row[i]  # 첫째 줄의 각 칸과 둘째 줄을 매핑

    def dfs(start):
        visited = [False] * (n + 1)  
        in_stack = [False] * (n + 1)  # 현재 경로에 있는 노드인지 확인
        cycle_nodes = set()
        stack = [start]

        while stack:
            node = stack[-1]
            if not visited[node]:
                visited[node] = True
                in_stack[node] = True
                next_node = graph[node]
                if not visited[next_node]:
                    stack.append(next_node)
                elif in_stack[next_node]:  # 사이클 발견
                    cycle_nodes.add(next_node)
                    while stack and stack[-1] != next_node:
                        cycle_nodes.add(stack.pop())
                    cycle_nodes.add(stack.pop())
            else:
                in_stack[node] = False
                stack.pop()

        return cycle_nodes

    result = set()
    for i in range(1, n + 1):
        if i not in result:  # 이미 포함된 노드는 건너뜀
            result.update(dfs(i))

    return sorted(result)

if __name__ == "__main__":
    n = int(input())
    second_row = [int(input()) for _ in range(n)]
    answer = find_cycles(n, second_row)
    print(len(answer))
    for num in answer:
        print(num)

       