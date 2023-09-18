ramData1 = 1010
ramData2 = 1110
IR = 0

opCode1 = 0
opCode2 = 0

if ramData1 > 0 and ramData2 > 0:
    IR = str(ramData1) + str(ramData2)
print(IR)

IR = int(IR)

if IR > 0:
    opCode1 = ramData1
    opCode2 = ramData2

print(opCode1)
print(opCode2)