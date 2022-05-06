
keyword = ['break', 'case', 'char', 'const', 'countinue', 'deafult', 'do', 'int', 'else', 'enum',  'float', 'for', 'goto',
           'if', 'long', 'return', 'short', 'signed', 'sizeof', 'static', 'switch', 'typedef', 'union', 'unsigned', 'void', 'while']
operators = ['+', '-', '*', '/', '%', '==', '!=', '>', '<', '>=', '<=',
             '&&', '||', '!', '&', '|', '^', '~', '>>', '<<', '=', '+=', '-=', '*=']
specialsymbol = ['@', '#', '$', '_', '!']
separator = [',', ':', ';', '\n', '\t', '{', '}', '(', ')', '[', ']']
library = ['<assert.h>', '<ctype.h>', '<locale.h>', '<math.h>', '<setjmp.h>',
           '<signal.h>', '<stdarg.h>', '<stdio.h>', '<stdlib.h>', '<string.h>', '<time.h>']
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

file = open('my.txt', 'r+')
contents = file.read()
splitCode = contents.split()
length = len(splitCode)
lineWise = contents.split('\n')
for t in range(0, len(lineWise)):
    splitCode1 = lineWise[t].split()
    print(f'Line number {t+1}')
    for j in range(0, len(splitCode1)):
        if splitCode1[j] in keyword:
            print("Keywords -->", splitCode1[j])
            continue
        elif splitCode1[j] in operators:
            print("Operators --> ", splitCode1[j])
            continue
        elif splitCode1[j] in specialsymbol:
            print("Special Operators -->", splitCode1[j])
            continue
        elif splitCode1[j] in separator:
            print("Separators -->", splitCode1[j])
            continue
        elif splitCode1[j] in number:
            print("Numericals -->", splitCode1[j])
            continue
        elif ('#include' == splitCode1[j]):
            print("Header File -->", splitCode1[j])
            continue
        elif splitCode1[j] in library:
            print("Library -->", splitCode1[j])
            continue
        else:
            print("Identifier --> ", splitCode1[j])
    print('\n')
