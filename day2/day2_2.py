# coding: utf-8

#open file to read codes

with open('codes_day_2', 'r', newline='\n') as f:
    codigos = [i.strip() for i in f.readlines()]
    
f.close()

def dif_is1(w1, w2):
    pares = [l1 != l2 for l1,l2 in zip(w1,w2)]
    return sum(pares)==1

ex1 = [
'abcde',
'fghij',
'klmno',
'pqrst',
'fguij',
'axcye',
'wvxyz'
]

ex2 = ex1[:]

for w1 in ex1:
    ex2.pop(0)
    for w2 in ex2:
        if dif_is1(w1,w2):
            print( w1,w2)

codigos2 = codigos[:]

for w1 in codigos:
    codigos2.pop(0)
    for w2 in codigos2:
        if dif_is1(w1,w2):
            pals = [w1,w2]


print(pals[0])
print(pals[1])

comun = ''
for i in [l for l,l2 in zip(pals[0],pals[1]) if l == l2]:
    comun+=i

print(comun)


