import math


ds = [(1, 0), (-1, 0), (0, 1), (0, -1)] 
inf_triple = (math.inf, math.inf, math.inf)

with open('in.txt', 'r') as fin, open('out.txt', 'w') as fout:
    def check(p, i, j):
        return (matrix[i][j], i, j) if 0 <= i < m and 0 <= j < n and p < matrix[i][j] else inf_triple

    def get_next_move(p, i, j):
        res = min(check(p, i + di, j + dj) for di, dj in ds)
        return res if res != inf_triple else None

    m, n = map(int, fin.readline().strip().split())
    matrix = []
    start = inf_triple 
    for i in range(m):
        xs = list(map(int, fin.readline().strip().split()))
        for j in range(n):
            start = min(start, (xs[j], i, j))
        matrix.append(xs)

    p, i, j = start
    ans = p
    next_move = get_next_move(p, i, j)
    while next_move:
        p, i, j = next_move
        ans += p
        next_move = get_next_move(p, i, j)
    print(ans, file=fout)
