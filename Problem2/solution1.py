with open('in.txt', 'r') as fin, open('out.txt', 'w') as fout:
    for _ in range(int(fin.readline().strip())):
        n, *xs = map(int, fin.readline().strip().split())
        print('%.2f' % (sum(xs) / n), file=fout)

