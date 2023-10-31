with open('in.txt', 'r') as fin, open('out.txt', 'w') as fout:
    def to_prefix(exp):
        n = len(exp)
        open_brackets = 0
        for i in range(n):
            if exp[i] == '(':
                open_brackets += 1
            elif exp[i] == ')':
                open_brackets -= 1
            elif not open_brackets:
                break
        else:
            exp = exp[1:-1]
            n -= 2

        first_additive, first_multiplicative = None, None
        for i in range(n):
            if exp[i] == '(':
                open_brackets += 1
            elif exp[i] == ')':
                open_brackets -= 1
            elif not open_brackets:
                if exp[i] == '+' or exp[i] == '-':
                    first_additive = i
                    break
                elif not first_multiplicative and (exp[i] == '*' or exp[i] == '/'):
                    first_multiplicative = i

        if first_additive:
            return exp[first_additive] + to_prefix(exp[:first_additive]) + to_prefix(exp[first_additive + 1:])

        if first_multiplicative:
            return exp[first_multiplicative] + to_prefix(exp[:first_multiplicative]) + to_prefix(exp[first_multiplicative + 1:])

        return exp

    print(to_prefix(fin.readline().strip()), file=fout)
