with open('data','r') as f:
    rows = [(i.replace('\n','').split(' ')[1],
           i.replace('\n','').split(' ')[7]
           ) for i in f.readlines()]

f.close()

print(rows[0:5])
print(len(rows))

total = []
for i in rows:
    total.append(i[0])
    total.append(i[1])

total = list(set(total))

print(len('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))



print(total)
print(len(total))

# example:
# [('A', 'R'), ('C', 'K'), ('H', 'G'), ('R', 'Z')]
# A before R, C before K, ...

diccionario = {}
for primero,segundo in rows:
    if segundo not in diccionario:
        diccionario[segundo]=[primero]
    else:
        diccionario[segundo].append(primero)

print(diccionario)

disponibles = []
for letra in total:
    if letra not in diccionario:
        disponibles.append(letra)

disponibles.sort()

print(disponibles)


pfinal = ''
while len(pfinal)<26:
    nueva = disponibles.pop(0)
    for entrada in diccionario:
        if nueva in diccionario[entrada]:
            diccionario[entrada].remove(nueva)
    borrar = []
    for entrada in diccionario:
        if len(diccionario[entrada])==0:
            disponibles.append(entrada)
            borrar.append(entrada)

    for i in borrar:
        del diccionario[i]

    pfinal+= nueva
    disponibles.sort()
    
print(pfinal)
