from collections import defaultdict
from heapq import heappush, heappop


with open('in.txt', 'r') as fin, open('out.txt', 'w') as fout:
    n, *lines = fin.readlines()
    n = int(n.strip())
    graph = defaultdict(list)
    for line in lines:
        a, b, w = map(int, line.strip().split())
        graph[a].append((w, b))
        graph[b].append((w, a))
    
    heap, visited = [(0, 0)], set()
    total = 0
    while len(visited) < n:
        weight, node = heappop(heap)
        if node in visited:
            continue
        visited.add(node)
        total += weight

        for neighbor in graph[node]:
            heappush(heap, neighbor)
    
    print(str(total), file=fout)
