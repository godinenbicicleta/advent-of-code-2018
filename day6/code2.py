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
malla = [[i,j] for i in range(x_min, x_max+1) for j in range(y_min,y_max+1)]

#manhattan distance:
def distance(p1,p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])


region=0

for m in malla:
    subtotal = 0
    for point in coordinates:
        subtotal += distance(point,m)
        if subtotal>=10000:
            break
    if subtotal< 10000:
        region+=1

print(region)
print(len(malla))            
