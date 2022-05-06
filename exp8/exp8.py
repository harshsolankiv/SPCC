
from prettytable import PrettyTable


def whileloop(code):
    fc = []
    idx = None
    for i in range(len(code)):
        just = code[i]
        if 'while' in just:
            idx = i
            newid = just.index('(')
            end_idx = just.index(')')
            bool_condn = ''.join(just[newid:end_idx + 1])
            fc.append('if !{} goto({})'.format(bool_condn, None))
            idx = i
        elif '}' in just:
            fc.append('goto({})'.format(idx + 1))
            fc[idx] = fc[idx].replace('None', str(i + 2))
            idx = None
        else:
            fc.append(just)
    return fc


with open('code.txt') as f:
    code = f.readlines()
print('\nGiven while-loop code is:')
print(''.join(code))
ans = []
for i in range(len(code)):
    if code[i] != '\n':
        if code[i][-1] == '\n':
            ans.append(code[i][:-1].strip())
        else:
            ans.append(code[i].strip())
fans = whileloop(ans)
fans.append('END')
print('\nThree address code for given while-loop code is:')
show = PrettyTable()
show.field_names = ['Serial No', 'Three address code']
for i in range(len(fans)):
    show.add_row([i + 1, fans[i]])
print(show)
