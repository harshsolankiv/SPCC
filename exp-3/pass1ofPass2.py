import re

class MOT:

    def __init__(self,mnemonic,binaryop,insLength,insFormat):
        self.mnemonic = mnemonic
        self.binaryop = binaryop
        self.insLength = insLength
        self.insFormat = insFormat

class POT:

    def __init__(self,psop,address):
        self.psop = psop
        self.address = address

class ST:

    def __init__(self,symbol,value,length,relocation):
        self.symbol = symbol
        self.value = value
        self.length = length
        self.relocation = relocation

def removeValuesFromList(theList,val):
    return [value for value in theList if value!=val]

Mlist = []
Mlist1 = []
Mlist.append(MOT('L','58','10','001'))
Mlist.append(MOT('A','5A','10','001'))
Mlist.append(MOT('ST','50','10','001'))

Plist = []
Plist1 = []
Plist.append(POT('START','P1START'))
Plist.append(POT('USING','P1USING'))
Plist.append(POT('DC','P1DC'))
Plist.append(POT('DS','P1DS'))
Plist.append(POT('END','P1END'))

STlist = []

f = open("SampleCodeForPass1.txt","rt")
addr = 0

for line in f:
    s = re.split(" |\t|\n",line)
    s = removeValuesFromList(s,"")
    print(s)
    if(len(s)==2):
        operands = s[1].split(',')
        if(s[0]!='USING'):
            addr+=4
        for item in Plist:
            if(item.psop == s[0]):
                Plist1.append(POT(s[0],item.address))
        for item in Mlist:
            if(item.mnemonic == s[0]):
                Mlist1.append(MOT(s[0],item.binaryop,item.insLength,item.insFormat))
    else:
        if(len(s)==3):
            if(s[1]=="START"):
                STlist.append(ST(s[0],str((addr)),0,'R'))
            else:
                STlist.append(ST(s[0],str((addr)),4,'R'))
            if(s[1]!='START'):
                addr+=4
        for i in range(len(s)):
            for item in Plist:
                if(item.psop == s[i]):
                    Plist1.append(POT(s[i],item.address))
            for item in Mlist:
                if(item.mnemonic == s[i]):
                    Mlist1.append(MOT(s[i],item.binaryop,item.insLength,item.insFormat))

print()
print("SYMBOL TABLE")
for item in STlist:
    print(item.symbol+"\t\t"+item.value+"\t\t"+str(item.length)+"\t\t"+item.relocation)
print()
print("PSEUDO OPERATION TABLE")
for item in Plist1:
    print(item.psop+"\t\t"+item.address)
print()
print("MACHINE OPERATION TABLE")
for item in Mlist1:
    print(item.mnemonic+"\t\t"+item.binaryop+"\t\t"+item.insLength+"\t\t"+item.insFormat)
