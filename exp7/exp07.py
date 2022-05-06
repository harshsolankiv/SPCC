class macronametable():
    def __init__(self, index, macroname, mdtindex):
        self.index = index
        self.macroname = macroname
        self.mdtindex = mdtindex

class MDT():
    def __init__(self, index, card):
        self.index = index
        self.card = card

class ALA():
    def __init__(self, index, args):
        self.index = index
        self.args = args

macronametableList = []
mdtList = []
alaList = []
lineList=[]

if __name__ == '__main__':
    f = open("macro.txt", "rt")
    addr = 0
    macronametableindex = 0
    mdtindex = 0
    alaindex = 0
    counter = 0
    while line := f.readline():
        #print(line[:-1])
        line = line.split()
        lineList.append(line)

    for i, line in enumerate(lineList):
        if("MACRO" in lineList[i-1]):
            counter += 1
            macronametableList.append(macronametable(macronametableindex, line[0], mdtindex))
            mdtList.append(MDT(mdtindex, " ".join(line)))
            alaList.append(ALA(alaindex, " ".join(line[1:])))
            macronametableindex += 1
            mdtindex += 1
            alaindex += 1
        elif(counter > 0 and "MACRO" not in line):
            mdtList.append(MDT(mdtindex, " ".join(line)))
            mdtindex += 1
        if("MEND" in line):
            counter -= 1

    print("\nmacronametable Table:-")
    print("{:^12}{:^12}{:^12}".format("index", "macro name", "mdt index"))
    for item in macronametableList:
        print("{:^12}{:^12}{:^12}".format(
            item.index, item.macroname, item.mdtindex))

    print("\nMDT Table:-")
    print("{:^12}{:^12}".format("index", "card")),
    for item in mdtList:
        print("{:^12}{:^12}".format(item.index, item.card))

    print("\nALA Table:-")
    print("{:^12}{:^12}".format("index", "arguments"))
    for item in alaList:
        print("{:^12}{:^12}".format(item.index, item.args))