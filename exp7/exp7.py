import re
with open('macro.txt') as f:
    sent_tokens = f.readlines()
for i, line in enumerate(sent_tokens):
    tokens = line.split(' ')
    print(f"LINE {i + 1}:{tokens}")


def pass1():
    macro_name_table, arg_list_arr, alas, macro_def_table = (
        [] for i in range(4))
    mdt_index, mnt_index, ala_index = (0 for i in range(3))
    flag = 0
    for sent in sent_tokens:
        mdt_entry = {'Index': 0, 'Definition': "null"}
        mnt_entry = {'Index': 0, 'Macro Name': "null", 'MDT Index': 0}
        ala_entry = {'Index': 0, 'Argument': "null", 'Value': '-'}
        sent = sent.strip()

        sent = sent.replace(", ", ",")
        if (';' in sent):
            sent = re.sub(';.*', '', sent)
        word_tokens = re.findall(r"[\S]+", sent)
        if ("MACRO" in sent):
            flag = 1
            continue
        if flag >= 1:
            # sent = sent.replace("\t", " ")
            mdt_index += 1
            mdt_entry = {'Index': mdt_index, 'Definition': sent}
            macro_def_table.append(mdt_entry)
            if flag == 1:
                macro_name = word_tokens[0]
                mnt_index += 1
                operands = word_tokens[1].split(',')
                mnt_entry = {'Index': mnt_index, 'Macro Name': macro_name, 'MDT Index':
                             mdt_index}
                macro_name_table.append(mnt_entry)
                for operand in operands:
                    ala_index += 1
                    if '=' in operand:
                        ala_entry = {'Index': ala_index, 'Argument': re.findall('(.*)=', operand)[0],
                                     'Value': re.findall('=(.*)', operand)[0]}
                    else:
                        ala_entry = {'Index': ala_index,
                                     'Argument': operand, 'Value': '-'}
                    alas.append(ala_entry)
                arg_list_arr.append(alas)
            flag += 1
        if "MEND" in sent:
            flag = 0
            alas = []
            ala_index = 0
    print("\n\nMacro Name Table :- \n")
    print('{:10}'.format("Index"), '{:20}'.format(
        "Macro Name"), '{:20}'.format("MDT Index"))
    for x in macro_name_table:
        print('{:10}'.format(str(x["Index"])), '{:20}'.format(
            x["Macro Name"]), '{:20}'.format(str(x["MDT Index"])))
    for alas in arg_list_arr:
        print("\n\nArgument List Array for " +
              macro_name_table[arg_list_arr.index(alas)]["Macro Name"] + ":- \n")
        print('{:10}'.format("Index"), '{:20}'.format(
            "Argument"), '{:20}'.format("Value"))
        for x in alas:
            print('{:10}'.format(str(x["Index"])), '{:20}'.format(x["Argument"]),
                  '{:20}'.format(x["Value"]))
    print("\n\nMacro Definition Table :- \n")
    print('{:10}'.format("Index"), '{:20}'.format("Definiton"))
    for x in macro_def_table:
        print('{:10}'.format(str(x["Index"])), '{:20}'.format(x["Definition"]))


pass1()
