with open('data') as f:
    data = f.read()

f.close()

lines = [d for d in data.split('\n') if len(d)>0]

for n,l in enumerate(lines):
    print(l)
    if n>10:
        break

before = [eval(i.replace('Before: ','')) for i in lines[::3]]
instructions = [[int(k) for k in i.split()] for i in lines[1::3]]
after = [eval(i.replace('After:  ','')) for i in lines[2::3]]

steps = zip(before, instructions, after)

for i in steps:
    print(i)
    break


# steps:
#        before     instructions      after
#    ([0, 2, 2, 2], [11, 3, 3, 3], [0, 2, 2, 0])
#
def parser(step): 
    before = step[0]
    instructions = step[1]
    opcode = instructions[0]
    registerA = instructions[1]
    registerB = instructions[2]
    output = instructions[3]
    after = step[-1]
    return {'before': before, 'instructions': instructions, 'opcode':opcode, 
            'registerA': registerA, 'registerB': registerB, 'registerC' : output,
            'after': after}

#Addition:

#addr (add register) stores into register C the result of adding register A and register B.
def addr(step):
    data = parser(step)
    before = data['before'][:]
    result = before[:]
    result[data['registerC']] = before[data['registerA']]+ before[data['registerB']]
    return result

print('')
print('======= test addr ====')
for i in steps:
    print(i)
    print('stores into register C the result of adding resgister A and register B')
    print(addr(i))
    break


#addi (add immediate) stores into register C the result of adding register A and value B.

def addi(step):
    data = parser(step)
    before = data['before'][:]
    result = before[:]
    result[data['registerC']] = before[data['registerA']] + data['registerB']
    return result

print('')
print('======= test addi ====')
for i in steps:
    print(i)
    print('stores into register C the result of adding resgister A and value B')
    print(addi(i))
    break


#Multiplication:

#mulr (multiply register) stores into register C the result of multiplying register A and register B.
def mulr(step):
    data = parser(step)
    before = data['before'][:]
    result = before[:]
    result[data['registerC']] = before[data['registerA']] * before[data['registerB']]
    return result

#muli (multiply immediate) stores into register C the result of multiplying register A and value B.
def muli(step):
    data = parser(step)
    before = data['before'][:]
    result = before[:]
    result[data['registerC']] = before[data['registerA']] * data['registerB']
    return result

#Bitwise AND:

#banr (bitwise AND register) stores into register C the result of the bitwise AND of register A and register B.
def banr(step):
    data = parser(step)
    before = data['before'][:]
    result = before[:]
    result[data['registerC']] = before[data['registerA']] & before[data['registerB']]
    return result
#bani (bitwise AND immediate) stores into register C the result of the bitwise AND of register A and value B.
def bani(step):
    data = parser(step)
    before = data['before'][:]
    result = before[:]
    result[data['registerC']] = before[data['registerA']] & data['registerB']
    return result
#Bitwise OR:

#borr (bitwise OR register) stores into register C the result of the bitwise OR of register A and register B.
def borr(step):
    data = parser(step)
    before = data['before'][:]
    result = before[:]
    result[data['registerC']] = before[data['registerA']] | before[data['registerB']]
    return result
#bori (bitwise OR immediate) stores into register C the result of the bitwise OR of register A and value B.
def bori(step):
    data = parser(step)
    before = data['before'][:]
    result = before[:]
    result[data['registerC']] = before[data['registerA']] | data['registerB']
    return result
#Assignment:

#setr (set register) copies the contents of register A into register C. (Input B is ignored.)
def setr(step):
    data = parser(step)
    before = data['before'][:]
    result = before[:]
    result[data['registerC']] = before[data['registerA']] 
    return result
#seti (set immediate) stores value A into register C. (Input B is ignored.)
def seti(step):
    data = parser(step)
    before = data['before'][:]
    result = before[:]
    result[data['registerC']] = data['registerA']
    return result
#Greater-than testing:

#gtir (greater-than immediate/register) sets register C to 1 if value A is greater than register B. Otherwise, register C is set to 0.
def gtir(step):
    data = parser(step)
    before = data['before'][:]
    result = before[:]
    if data['registerA'] > before[data['registerB']]:
        result[data['registerC']] = 1
        return result
    result[data['registerC']] = 0
    return result

#gtri (greater-than register/immediate) sets register C to 1 if register A is greater than value B. Otherwise, register C is set to 0.
def gtri(step):
    data = parser(step)
    before = data['before'][:]
    result = before[:]
    if before[data['registerA']] > data['registerB']:
        result[data['registerC']] = 1
        return result
    result[data['registerC']] = 0
    return result
#gtrr (greater-than register/register) sets register C to 1 if register A is greater than register B. Otherwise, register C is set to 0.
def gtrr(step):
    data = parser(step)
    before = data['before'][:]
    result = before[:]
    if before[data['registerA']] > before[data['registerB']]:
        result[data['registerC']] = 1
        return result
    result[data['registerC']] = 0
    return result
#Equality testing:

#eqir (equal immediate/register) sets register C to 1 if value A is equal to register B. Otherwise, register C is set to 0.
def eqir(step):
    data = parser(step)
    before = data['before'][:]
    result = before[:]
    if data['registerA'] == before[data['registerB']]:
        result[data['registerC']] = 1
        return result
    result[data['registerC']] = 0
    return result
#eqri (equal register/immediate) sets register C to 1 if register A is equal to value B. Otherwise, register C is set to 0.
def eqri(step):
    data = parser(step)
    before = data['before'][:]
    result = before[:]
    if before[data['registerA']] == data['registerB']:
        result[data['registerC']] = 1
        return result
    result[data['registerC']] = 0
    return result
#eqrr (equal register/register) sets register C to 1 if register A is equal to register B. Otherwise, register C is set to 0.
def eqrr(step):
    data = parser(step)
    before = data['before'][:]
    result = before[:]
    if before[data['registerA']] == before[data['registerB']]:
        result[data['registerC']] = 1
        return result
    result[data['registerC']] = 0
    return result


operators = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti,
gtir, gtri, gtrr ,eqir, eqri, eqrr]



conteos = 0
for step in steps:
    conteo = 0
    for operator in operators:
        print('step: ',step[-1],'result :',operator(step)) 
        if step[-1] == operator(step):
            conteo += 1
    if conteo >=3:
        conteos+=1
print(conteos)


steps = zip(before, instructions, after)

revisar = len(list(steps))
import itertools
print(revisar)

candidatos = {}
for operator in operators:
    candidatos[operator] = []
    steps = list(zip(before, instructions, after))
    for i in range(16):
        bien = 0
        revisar = len([m for m in steps if m[1][0] == i])
        for step in steps:
            if step[2] == operator(step) and step[1][0] == i:
                bien+=1
        print(operator,bien,i, revisar)
        if bien == revisar:
            candidatos[operator].append(i)
candi = sorted(
list(candidatos.items()),
key = lambda x: len(x[1])) 

for i in candi:
    print(i[0], ':', i[1])


diccionario = {
9:addi ,
0:mulr ,
12:borr ,
1:addr ,
15:bori ,
14:seti ,
4:muli ,
5:setr ,
2:banr ,
8:eqrr ,
13:bani ,
10:gtir ,
7:gtri ,
11:gtrr ,
6:eqri ,
3:eqir 
}

with open('data2','r') as f:
    data2 = f.read()

f.close()

stepis  = [[int(i) for i in k.split()] for k in data2.split('\n')]

# steps:
#        before     instructions      after
#    ([0, 2, 2, 2], [11, 3, 3, 3], [0, 2, 2, 0])
#
print(stepis[-1])

for num,linea in enumerate(stepis[:-1]):
    if num == 0:
        step = ([0,0,0,0], linea, None)
        print([0,0,0,0], ' --> ', diccionario[linea[0]](step)) 
        before = diccionario[linea[0]](step)
        continue
    print('')
    print(before, ' --> ')
    print(linea)
    before = diccionario[linea[0]]((before, linea, None))
    print(before)

print(before) 
        



