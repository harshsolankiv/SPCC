OPERATORS = set(['+', '-', '*', '/', '(', ')'])
PRI = {'+': 1, '-': 1, '*': 2, '/': 2}


def infix_to_postfix(formula):
    stack = []
    output = ''
    for ch in formula:
        if ch not in OPERATORS:
            output += ch
        elif ch == '(':
            stack.append('(')
        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
                stack.pop()  # pop '('
        else:
            while stack and stack[-1] != '(' and PRI[ch] <= PRI[stack[-1]]:
                output += stack.pop()
            stack.append(ch)
    while stack:
        output += stack.pop()
    print(f'POSTFIX: {output}')
    return output


def generate3AC(pos):
    exp_stack = []
    t = 1
    for i in pos:
        if i not in OPERATORS:
            exp_stack.append(i)
        else:
            print(f't{t} := {exp_stack[-2]} {i} {exp_stack[-1]}')
            exp_stack = exp_stack[:-2]
            exp_stack.append(f't{t}')
            t += 1


def generate3ACTable(pos):
    exp_stack = []
    t = 1
    for i in pos:
        if i not in OPERATORS:
            exp_stack.append(i)
        else:
            print(f' {i}\t|\t{exp_stack[-2]}\t|\t{exp_stack[-1]}\t|\tt{t} ')
            exp_stack = exp_stack[:-2]
            exp_stack.append(f't{t}')
            t += 1


print("")
expres = input("INPUT THE EXPRESSION: ")
pos = infix_to_postfix(expres)
generate3AC(pos)
print("\n-----------Quadruple Table----------------\n")
print("op\t|\targ1\t|\targ2\t|\tResult\n")
generate3ACTable(pos)
