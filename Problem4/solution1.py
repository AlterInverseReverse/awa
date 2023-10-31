with open('in.txt', 'r') as fin, open('out.txt', 'w') as fout:
    command = fin.readline().strip()
    if len(command) > 50:
        print('輸入錯誤', file=fout)
    else:
        print(str(int(eval(command)))[-4:].lstrip('0'), file=fout)
