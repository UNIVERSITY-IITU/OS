
input_ = ['0x0000b128', '0x0000b12c', '0x0000b130']

memory = {
    input_[0]:'0x0200ec00',
    input_[1]:'0x0300ec04',
    input_[2]:'0x0100ec08',

    '0x0200ec00':'0x00000016',
    '0x0300ec00':'0x0000009E',
    '0x0100ec00':'0x00000000'
}

cpu = [
    list(memory.keys())[0],#pc
    '',                    #ac
    ''                     #ir
]
'''
* 1  store ac to mem
* 2  load mr-ir
* 3 add ac+mem
'''

for i, j in memory.items():
    try:
        cpu[0] = i
        cpu[2] = memory[cpu[0]]

        if cpu[2][3:4] == '2':
            cpu[1] = memory[cpu[2]]
        elif cpu[2][3:4] == '3':
            hint1 = int(cpu[1][8:],16)
            hint2 = int(memory[cpu[0]][8:],16)
            hex_ = hex(hint1 + hint2)
            cpu[1] = hex_[:2] + '000000' + hex_[2:]
        elif cpu[2][3:4] == '1':
            memory[cpu[0]] = cpu[1]
        else:
            break
        print('################')
        print("PC {0}\nAC {1}\nIR {2}\n".format(cpu[0],cpu[1],cpu[2]))
        for i , j in memory.items():
            print('{0} : {1}'.format(i,j))
        print('\n\n')
    except Exception as e:
        print(e)
    
'''
################
PC 0x0000b128
AC 0x00000016
IR 0x0200ec00

0x0000b128 : 0x0200ec00
0x0000b12c : 0x0300ec04
0x0000b130 : 0x0100ec08
0x0200ec00 : 0x00000016
0x0300ec00 : 0x0000009E
0x0100ec00 : 0x00000000



################
PC 0x0000b12c
AC 0x0000001a
IR 0x0300ec04

0x0000b128 : 0x0200ec00
0x0000b12c : 0x0300ec04
0x0000b130 : 0x0100ec08
0x0200ec00 : 0x00000016
0x0300ec00 : 0x0000009E
0x0100ec00 : 0x00000000



################
PC 0x0000b130
AC 0x0000001a
IR 0x0100ec08

0x0000b128 : 0x0200ec00
0x0000b12c : 0x0300ec04
0x0000b130 : 0x0000001a
0x0200ec00 : 0x00000016
0x0300ec00 : 0x0000009E
0x0100ec00 : 0x00000000
'''