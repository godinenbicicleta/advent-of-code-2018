# load coordinates
coordinates=[]

with open('data','r') as f:
    for row in f:
        x,y = row.strip().split(',')
        x = int(x)
        y = int(y)
        coordinates.append((x,y))

print(coordinates[0:3])

# find extent of coordinates
x_max = max([x for x,_ in coordinates])
x_min = min([x for x,_ in coordinates])

y_max = max([y for _,y in coordinates])
y_min = min([y for _,y in coordinates])

#create empty array for the extent:


#manhattan distance:
def distance(p1,p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

print(len(coordinates))

#get nearest neighbours

lista_no_cambiaron =[]
cambiaron_lista = []
for k in range(0,200):
    malla = [[i,j] for i in range(x_min-k, x_max+1+k) for j in range(y_min+1-k,y_max+k+1)]
    areas = {p:0 for p in coordinates}
    print('malla: ', len(malla))
    
    for grid in malla:
        mind = 10000000000
        for point in coordinates:
            d = distance(grid,point)
            if d < mind:
                mind = d
                vecinos = 0
                vecino = point

            elif d == mind:
                vecinos += 1
        
        if vecinos == 0:
            areas[vecino]+=1

    cambiaron_lista.append(areas)

    if len(cambiaron_lista)>2:
        #cuantos cambiaron?
        penultimo = cambiaron_lista[-2]
        ultimo = cambiaron_lista[-1]
        no_cambiaron = 0
        cambiaron=0
        incambiables=[]
        for p in coordinates:
            if penultimo[p]==ultimo[p]:
                no_cambiaron+=1
                if areas[p]>0:
                    incambiables.append(p)
            else:
                cambiaron+=1
        lista_no_cambiaron.append(no_cambiaron)
        print(no_cambiaron, cambiaron)

    if (len(lista_no_cambiaron)>10 and cambiaron<len(coordinates) and
        lista_no_cambiaron[-1] == lista_no_cambiaron[-2] and 
        lista_no_cambiaron[-3]):
        break 



    print('ronda: ',k)



print(max([areas[i] for i in areas if i in incambiables]))
print(areas)
print(cambiaron_lista)
