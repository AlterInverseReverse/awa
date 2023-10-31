from collections import defaultdict
from heapq import heappush, heappop


with open('in.txt', 'r') as fin, open('out.txt', 'w') as fout:
    n = int(fin.readline().strip())
    graph = defaultdict(list)
    for _ in range(n):
        a, b, w = map(int, fin.readline().strip().split())
        graph[a].append((w, b))
        graph[b].append((w, a))
    
    j, k = map(int, fin.readline().strip().split())
    heap, visited = [(0, j)], set()
    minimum_required = 0
    while heap and k not in visited:
        weight, node = heappop(heap)
        if node in visited:
            continue
        visited.add(node)
        minimum_required = max(minimum_required, weight)

        for neighbor in graph[node]:
            heappush(heap, neighbor)

    print(str(minimum_required if k in visited else -1), file=fout)
