import datetime

#open file with info
with open('info_day_4','r') as f:
    raw = [i.replace('\n','') for i in f.readlines()]

f.close()

#see what the lines look like
for i in range(5):
    print(raw[i])

#see character position
print('first - : ',raw[i].index('-'))
print('first space : ',raw[i].index(' '))
print('first : ',raw[i].index(':'))

#first we need to give format and order the data
def parse_data(linea):
    year =int( linea[1:5])
    month =int( linea[6:8])
    day =int( linea[9:11])

    hour =int( linea[12:14])
    minute =int( linea[15:17])

    return datetime.datetime(year, month, day,
            hour, minute)

#see if we got datetime correct
print(parse_data(raw[0]))
print(parse_data(raw[-1]))

# add datetime info and sort the data
entries = sorted([[parse_data(j),j[19:]] for j in raw],
        key = lambda x: x[0])

for i in range(5):
    print(entries[i])


print("############")

#add guard ID
def add_guard_id(lineas):
    con_id = lineas[:]
    for lin in con_id:
        if '#' == lin[1][6]:
            guard_id = lin[1][7:11]
            lin.append(guard_id)
        else:
            lin.append(guard_id)
    return con_id

con_id = add_guard_id(entries)

for i in range(10):
    print(con_id[i])



guards = {}

for entri in con_id:
    guard_id = entri[-1]

    if "#" ==entri[1][6] and guard_id not in guards:
        guards[guard_id] = {'tiempo_dormido':0,
        'count_minutos':{}}

    if entri[1][0] == 'f':
        min_inicial = entri[0].minute
    if entri[1][0] == 'w':
        min_final = entri[0].minute
        guards[guard_id]['tiempo_dormido']+= min_final-min_inicial
        for i in range(min_inicial, min_final):
            if i not in guards[guard_id]['count_minutos']:
                guards[guard_id]['count_minutos'][i] = 1
            else:
                guards[guard_id]['count_minutos'][i] += 1


print(guards['2543'])
print(guards['3571'])
print(guards)

maximo = 0
for i in guards:
    if guards[i]['tiempo_dormido']>maximo:
        maximo = guards[i]['tiempo_dormido']
        id_max = i

print("###")

print(id_max, guards[id_max])

print(
sorted(list(guards[id_max]['count_minutos'].items()),
key = lambda x: x[1])[-1]
)

print(id_max, 
int(sorted(list(guards[id_max]['count_minutos'].items()),
key = lambda x: x[1])[-1][0])*int(id_max))


max_minutos = 0
for id_guardia in guards:
    try:
        minuti, veces = sorted(list(guards[id_guardia]['count_minutos'].items()),
        key = lambda x: x[1])[-1]
        if veces> max_minutos:
          max_minutos = veces
          max_minuti = minuti
          max_guard = id_guardia
    except:
        print(guards[id_guardia])


print('max_minutos: ', max_minutos)
print('max_minuti: ', max_minuti)
print('max_guard: ', max_guard)
print('answer: ', int(max_guard)*(max_minuti))




class entrada():
    def __init__(self, fecha ):
        pass
