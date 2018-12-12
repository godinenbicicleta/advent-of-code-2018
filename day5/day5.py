with open('info_day5','r') as f:
    pol = f.readline().strip()

print(pol[0:10])
print(pol[-10:])
print(len(pol))


def checar_uno(palabra):
    for i,_ in enumerate(palabra[:-1]):
        if palabra[i].islower():
            if palabra[i].upper() == palabra[i+1]:
                return True
        elif palabra[i].isupper():
            if palabra[i].lower() == palabra[i+1]:
                return True
    return False


def reaccion(elemento):
    palabra = elemento[:]
    while  checar_uno(palabra):
        for indice,_  in enumerate(palabra[:-1]):
            if len(palabra)<100:
                print(palabra)
            try:
                if (
            (
              palabra[indice].islower() and 
              palabra[indice].upper() == palabra[indice+1]
            )
            or(
              palabra[indice].isupper() and
              palabra[indice].lower() == palabra[indice+1]
            )
            ):
                    palabra = palabra[:indice]+palabra[indice+2:]
            except:
                pass
        
    return len(palabra)
            

print(checar_uno('dabAcCaCBAcCcaDA'))
prueba = reaccion('dabAcCaCBAcCcaDA')
print(prueba)


lfinal = reaccion(pol)
print('resultado: ',lfinal)



mini = 11814
for i in 'abcdefghijklmnopqrstuvwxyz' :
    print(i)
    candidato = reaccion(pol.replace(i,'').replace(i.upper(),''))
    if candidato < mini:
        mini = candidato
        current = i


print(mini,current)
