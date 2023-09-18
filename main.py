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

opCode1 = True
opCode2 = True

address14 = 0
if opCode1 and opCode2 != True:
    address14 = opCode1

print(address14)

if opCode1 == True or opCode2 != True:
    address14 = 1010
print(address14)
