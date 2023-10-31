import math


with open('in.txt', 'r') as fin, open('out.txt', 'w') as fout:
    for _ in range(int(fin.readline().strip())):
        print(str(math.gcd(*map(int, fin.readline().strip().split()))), file=fout)
