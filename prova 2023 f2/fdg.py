def main():
    N, B = map(int, input().split())
    islands = [[] for _ in range(N + 1)]

    for _ in range(B):
        I, J, P = map(int, input().split())
        islands[I].append((J, P))
        islands[J].append((I, P))

    C = int(input())
    for _ in range(C):
        X, Y = map(int, input().split())
        max_passengers = dfs(X, Y, islands)
        print(max_passengers)

def dfs(start, end, islands):
    visited = set()
    max_passengers = float('inf')
    dfs_stack = [(start, float('inf'))]

    while dfs_stack:
        current, min_capacity = dfs_stack.pop()

        if current == end:
            max_passengers = min(max_passengers, min_capacity)
            continue

        visited.add(current)

        for neighbor, capacity in islands[current]:
            if neighbor not in visited:
                new_min_capacity = min(min_capacity, capacity)
                dfs_stack.append((neighbor, new_min_capacity))

    return max_passengers

if __name__ == "__main__":
    main()
