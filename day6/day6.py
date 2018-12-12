#get all the coordinates
coordinates = []

with open('info_day6', 'r') as f:
    for row in f:
        x,y = int(row.strip().split(',')[0]),int(row.strip().split(',')[1])
        coordinates.append((x,y))

# need to find all the grids that are closest to each coordiante
# using manhattan distance d = x+y
#    goal:
#      find maximum area that is not infinity

def distance(p1,p2):
    return abs(p1[0]-p2[0])+abs(p2[1]-p1[1])

#test manhattan distance
#should return 7
print('manhattan distance between (1,1) and (6,3) is: ', 
        distance((1,1,),(6,3)))

#get extent of coordinates
x_max, y_max = max([p[0] for p in coordinates]), max([p[1] for p in coordinates])
x_min, y_min = min([p[0] for p in coordinates]), min(p[1] for p in coordinates)

#print extent:
print(x_min, x_max)
print(y_min, y_max)

#look for duplicates:
if len(coordinates) == len(set(coordinates)):
    print('no hay duplicados')

# first determine which "points" area bounded, and which are not
# that way when the las of the bounded ones stops increasing in area
# we have a winner

# lets assume all points in the border are unbounded
# which ones are the border  points?

#create point class

class Point():
    def __init__(self, p):
        self.id = str(p)
        self.x = p[0]
        self.y = p[1]
        if (self.x == x_min or self.x == x_max 
            or self.y == y_min or self.y == y_max):
            self.bounded = True
        else:
            self.bounded = False


    def distance_to(self,other):
        return distance((self.x,self.y),(other[0], other[1]) )


class Malla():
    def __init__(self, points):
        self.points_dict = {point.id:point for point in points}
        self.grid = []

    def create_vecinos(self):
        self.vecinos = {}
        self.descartados = {}
        for p in self.points_dict:
            self.vecinos[self.points_dict[p].id]=[(self.points_dict[p].x,
            self.points_dict[p].y)]
            self.descartados[self.points_dict[p].id]= []
        print('vecinos creados')

    def fill_vecinos(self):
        self.len_inicial = {}
        for i in self.points_dict:
            if self.points_dict[i].bounded:
                self.len_inicial[self.points_dict[i].id] = 1
        print(self.len_inicial)
        seguimos = True
        candidatos_usados = []
        lili = 1
        while seguimos:
            print('iteracion ',lili)
            for p in self.points_dict:
                    candidatos = []
                    for vecino in self.vecinos[self.points_dict[p].id]:
                        c1x, c2x = vecino[0]+lili,vecino[0]-lili
                        c1y, c2y = vecino[1]+lili,vecino[1]-lili
                        candidatos_pre =set([(c1x,c1y),(c1x,c2y),(c2x,c1y),(c2x,c2y),
                        (vecino[0],c1y),(vecino[0],c2y),
                        (c1x,vecino[1]),(c2x,vecino[1])])
                        for ca in candidatos_pre:
                            if (ca not in self.vecinos[self.points_dict[p].id]
                                and ca not in
                                self.descartados[self.points_dict[p].id]):
                                candidatos.append(ca)
                    print(len(candidatos))
                    #para cada candidato
                    for c in candidatos:
                        if c not in  candidatos_usados:
                            #checamos en todos los puntos
                            for v in self.vecinos:
                                #si ya es vecino de alguien
                                if c in self.vecinos[v]:
                                    #vemos quien esta mas cerca
                                    if self.points_dict[p].distance_to(c)<self.points_dict[v].distance_to(c):
                                    #si p esta mas cerca, entonces es vecino de p
                                        self.vecinos[self.points_dict[p].id].append(c)
                                    if\
                                        (self.points_dict[p].distance_to(c) >= self.points_dict[v].distance_to(c)
                                        and c in
                                        self.vecinos[self.points_dict[p].id]):
                                        self.vecinos[self.points_dict[p].id].remove(c)
                                        self.descartados[self.points_dict[p].id].append(c)
                                else:
                                    self.vecinos[self.points_dict[p].id].append(c)
            lili+=1
            len_actual = {}
            for i in self.points_dict:
                if self.points_dict[i].bounded:
                    len_actual[i]=len(self.vecinos[i])
            if len_actual == self.len_inicial:
                break
            if len_actual != self.len_inicial:
                self.len_inicial = len_actual
                print(len_actual)

        max_len = 0
        for i in self.vecinos:
            if len(self.vecinos[i])>max_len:
                max_len = len(self.vecinos[i])

        return max_len


print(len(coordinates))
malla = Malla([Point(p) for p in coordinates])
malla.create_vecinos()
print(malla.fill_vecinos())
