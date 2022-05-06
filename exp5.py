n = int(input("Enter Number of productions "))
Sym = []
V = []
T = []
P = []
for i in range(n):
    prod = input("Enter production: ")
    v = prod[0]
    if v not in V:
        V.append(v)
        P.append([])
    if(v not in Sym):
        Sym.append(v)
    ind = V.index(v)
    for j in range(3, len(prod)):
        if(prod[j] not in Sym and prod[j] != '|' and prod[j] != 'ε'):
            Sym.append(prod[j])
    lst = prod[3:].split('|')
    for z in lst:
        P[ind].append(z)
for j in Sym:
    if j not in V:
        T.append(j)


First = []
for i in range(len(Sym)):
    First.append([])
Sym = []
Sym.extend(T)
Sym.extend(V)
eps = []
t = len(T)
for i in range(t):
    First[i].append(Sym[i])
for j in range(t, len(Sym)):
    for x in P[j-t]:
        if(x[0] in T):
            First[j].append(x[0])

    if('ε' in P[j-t]):
        First[j].append('ε')
        eps.append(V[j-t])
change = 1
while(change != 0):
    change = 0
    for j in range(t, len(Sym)):
        if(Sym[j] not in eps):
            for p in P[j-t]:
                flag = 0
                for k in p:
                    if(k not in eps):
                        flag = 1
                        break
                if(flag == 0):
                    First[j].append('ε')
                    eps.append(V[j-t])
                    change += 1
                    break

change = 1
while(change != 0):
    change = 0
    for j in range(t, len(Sym)):
        for p in P[j-t]:
            if(p != 'ε'):
                k = 0
                idx = Sym.index(p[k])
                for z in First[idx]:
                    if(z not in First[j] and z != 'ε'):
                        First[j].append(z)
                        change += 1
                while('ε' in First[idx] and k < len(p)):
                    k += 1
                    idx = Sym.index(p[k])
                    for z in First[idx]:
                        if (z not in First[j] and z != 'ε'):
                            First[j].append(z)
                            change += 1
print("Symbol   First-Pos")
for i in range(len(V)):
    print(V[i], "      ", First[t+i])
