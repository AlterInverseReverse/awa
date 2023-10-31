import operator


with open('in.txt', 'r') as fin, open('out.txt', 'w') as fout:
    catalan = [1]
    for _ in range(int(fin.readline().strip())):
        catalan.append(sum(map(operator.mul, catalan, reversed(catalan))))
    print(str(catalan[-1]), file=fout)
