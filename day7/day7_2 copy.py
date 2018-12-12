class Worker():
    def __init__(self, name):
        self.name = name
        self.ocupado = False

    def start(self,letra):
        self.ocupado = True
        self.waiting_time = duraciones[letra]

    def reduce(self):
        self.waiting_time -= 1
        if self.waiitng_time == 0:
            self.ocupado = False


# see if there are available workers
workers = []

for i in range(5):
    workers.append(Worker(i))

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

duraciones = {}
for pos,l in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    duraciones[l]=61+l

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
t = 0
while len(pfinal)<26:
    for worker in workers:
        if worker.ocupado == False:
            worker.start(disponibles.pop(0))
    if len(disponibles) == 0 or (
len([w for w in workers if not w.ocupado])==0
):
        t+=1
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
#assign letters and time to available workers



#se if there are available workers, if not, increase time by one, decrease
#waiting time by 1

#keep going until a worker is available

#when a worker becomes abailable, see what letters now become available

#assign letters to available workers and set waiting time

#no available workers then increase time, decrease waiting time

#add to available letters

#repeat until finished

