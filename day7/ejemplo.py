ejemplo = ['Step C must be finished before step A can begin.',
'Step C must be finished before step F can begin.',
'Step A must be finished before step B can begin.',
'Step A must be finished before step D can begin.',
'Step B must be finished before step E can begin.',
'Step D must be finished before step E can begin.',
'Step F must be finished before step E can begin.']

rows = [(i.replace('\n','').split(' ')[1],
           i.replace('\n','').split(' ')[7]
           ) for i in ejemplo]


print(rows)
print(len(rows))


# example:
# ['A', 'B', 'C', 'D', 'E', 'F'] 
# A before R, C before K, ...

#solution must be CABDFE

letras = []

for i in rows:
    letras.append(i[0])
    letras.append(i[1])


letras = list(set(letras))
letras.sort()

print('total letras ',letras)

posibles = []	

for letra in letras:
    if letra not in [i for _,i in rows]:
        posibles.append(letra)

print('psoibles inicial ',posibles)
#posibles contains the letters that don't need anything
#else to execute

orden = []
orden.append(posibles[0])

print('orden inidicial', orden)
print('rows ',rows)
# rows: [('C', 'A'), ('C', 'F'), ('A', 'B'), ('A', 'D'), ('B', 'E'), ('D', 'E'), ('F', 'E')]


contador = 0
contadormax = len(rows)
while len(orden)<len(letras)-1:
    candidatos=[]
    for ele,par in enumerate(rows):
        print(par)
        print('if ',par[0], ' in ',posibles)
        if par[0] in posibles:
            if par[1] not in [s[1] for s in rows if s!= rows[ele]]:
                candidatos.append(par[1])
                print('candidatos ',candidatos)
        print(' rows for ', rows)
    posibles+=candidatos            
    posibles = list(set(posibles))
    posibles.sort()
    print('los posibles ',posibles)
    print('rows while ',rows)
    for p in [i for i in posibles if i not in orden]:
        orden.append(p)
        break
        
    print('orden: ', orden)    

palabra = ''
for p in orden:
    palabra+=p

print('letras final ', letras)
for p in letras:
    if p not in palabra:
        palabra+=p

print(palabra)
