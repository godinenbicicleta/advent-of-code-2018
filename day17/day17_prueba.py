with open('data') as f:
    data = f.read()
f.close()

data2 = """......+.......
............#.
.#..#.......#.
.#..#..#......
.#..#..#......
.#.....#......
.#.....#......
.#######......
..............
....#.....#...
....#.....#...
....#.#.#.#...
....#.#.#.#...
....#.###.#...
....#.....#...
....#######...
..............
.............."""


terrain2 = [list(i) for i in data2.split('\n')]

print(terrain2)


terrain = [['.' for x in range(560)] for y in range(1650) ]


maxy = 0
maxx = 0
miny = 1000
minx = 300

for line in data.split('\n')[:-1]:
    #print(line)
    if line[0]=='x':
        x = int(line.split(',')[0].split('=')[1])
        y0 = int(line.split('y=')[1].split('..')[0])
        y1 = int(line.split('y=')[1].split('..')[1])
        for k in range(y0,y1+1):
            terrain[k][x] =  '#'

        if x > maxx:
            maxx = x
        if y1 > maxy:
            maxy = y1

        if x < minx:
            minx = x
        if y0 < miny:
            miny = y0

    if line[0]=='y':
        y = int(line.split(',')[0].split('=')[1])
        x0 = int(line.split('x=')[1].split('..')[0])
        x1 = int(line.split('x=')[1].split('..')[1])
        for k in range(x0,x1+1):
            terrain[y][k] = '#'


        if x1 > maxx:
            maxx = x1
        if y > maxy:
            maxy = y

        if x0 < minx:
            minx = x0
        if y < miny:
            miny = y

#add water source to terrain:
terrain[0][500]='+'

print(minx,maxx, miny,maxy)

with open('terrain.txt','w') as f:
    for y in terrain:
        f.write(''.join(y[240:]))
        f.write('\n')


class Tree():
    def __init__(self,rd, x,y):
        self.numchilds = 0
        self.rd = rd
        self.right_wall = False
        self.left_wall = False
        self.pos = [x,y]
        self.childs = []
        self.maxy = 16
        self.maxx = 13

    def move_down(self):
        #if you can move down, move all the way down
        if self.pos[1] == maxy-2:
            return None
        if self.rd[self.pos[1]+1][self.pos[0]] == '.':
            try:
                while self.rd[self.pos[1]+1][self.pos[0]] == '.':
                    self.rd[self.pos[1]+1][self.pos[0]]= '|'
                    self.pos[1] += 1
            #on the final position, change to - :
                self.rd[self.pos[1]][self.pos[0]]= '-'
            except IndexError:
                return None


    def move_right(self):
        if self.pos[1]== self.maxy-1:
            return None
        # if you can move to the side, move all the way:
        if (self.rd[self.pos[1]][self.pos[0]+1] == '.' and
            self.rd[self.pos[1]+1][self.pos[0]] != '.' ) :
            while (self.rd[self.pos[1]][self.pos[0]+1] == '.' and
            self.rd[self.pos[1]+1][self.pos[0]] != '.' ) :
                print(self.pos[0], self.pos[1])
                print(f'cambie {(self.pos[0]+1, self.pos[1])} a "-"')
                self.rd[self.pos[1]][self.pos[0]+1]= '-'
                self.pos[0] += 1
                print('di paso derecho')
                self.show()

            #take one more step if no wall
            if (self.rd[self.pos[1]][self.pos[0]+1] != '#'):  
                #self.rd[self.pos[1]][self.pos[0]+1]= '-'
                #self.pos[0] += 1
                self.right_wall = False
                return True
            return False
        return False

                
    def move_left(self):
        # if you can move to the side, move all the way:
        if self.pos[1]== self.maxy-1:
            return None
        if (self.rd[self.pos[1]][self.pos[0] - 1] == '.' and
            self.rd[self.pos[1]+1][self.pos[0]] != '.' ) :
            while (self.rd[self.pos[1]][self.pos[0] - 1] == '.' and
            self.rd[self.pos[1]+1][self.pos[0]] != '.' ) :
                print(f'cambie {(self.pos[0]-1, self.pos[1])} a "-"')
                self.rd[self.pos[1]][self.pos[0]-1]= '-'
                self.pos[0] -= 1
                print('di paso izquierdo')
                self.show()

            #take one more step if no wall
            if (self.rd[self.pos[1]][self.pos[0] - 1] != '#'):  
                #self.rd[self.pos[1]][self.pos[0] - 1]= '-'
                #self.pos[0] -= 1
                self.left_wall = False
                return True
            return False
        return False

    def go_up(self):
        if self.pos[1]== self.maxy:
            return None
        self.pos[1]-=1
        if self.rd[self.pos[1]][self.pos[0]] == '|':
            self.rd[self.pos[1]][self.pos[0]] = '~'

    
    def show(self):
        for i in self.rd:
            print(''.join(i))

    def play(self):
    # start by going down
    # save current position before moving:
        while (self.pos[1] < self.maxy and self.pos[0] < self.maxx and
            self.childs == []):
            self.move_down()
            if self.pos[1] == self.maxy-1:
                break
            current_position = (self.pos[0],self.pos[1])
            #try to go right:
            if self.rd[self.pos[1]][self.pos[0]+1] == '#':
                self.right_wall = True
                
            elif self.rd[self.pos[1]][self.pos[0]+1] == '.':
                if self.move_right(): #no wall, create new tree
                    #new tree
                    print(self.pos[0],self.pos[1])
                    self.childs.append(Tree(self.rd, self.pos[0], self.pos[1]))
                    self.numchilds += 1
                else: #found wall
                    self.right_wall = True
                    #reset position and turn to '~' previous steps:
                    while (self.pos[0],self.pos[1]) != current_position:
                        self.rd[self.pos[1]][self.pos[0]] = '~'
                        self.pos[0] -= 1
                    
                    self.rd[self.pos[1]][self.pos[0]] = '~'
                    #finished my trip to the right and returned to initial
                    #position, need to go left

            self.pos[0],self.pos[1] = current_position
            print(current_position) 
            #try to go left
        
            if self.rd[self.pos[1]][self.pos[0]-1] == '#':
                self.left_wall = True

            elif self.rd[self.pos[1]][self.pos[0]-1] == '.':
                if self.move_left(): #no wall, create new tree
                    #new tree
                    self.childs.append(Tree(self.rd, self.pos[0], self.pos[1]))
                    self.numchilds += 1
                else: #found wall
                    self.left_wall = True
                    #reset position and turn to '~' previous steps:
                    while (self.pos[0],self.pos[1]) != current_position:
                        self.rd[self.pos[1]][self.pos[0]] = '~'
                        self.pos[0] += 1
                    
                    self.rd[self.pos[1]][self.pos[0]] = '~'
                    #finished my trip to the left and returned to initial
                    #position, need to go up or down

            self.pos[0],self.pos[1] = current_position
            
            # if both walls, go up, repeat,
            if self.left_wall == True and self.right_wall == True:
                print('going up')
                self.go_up()
                current_position = (self.pos[0],self.pos[1])
            print(self.childs)
            for child in self.childs:
                try:
                    child.play()
                except:
                    continue

            self.show()








prueba = Tree(terrain2, 6,0)
prueba.play()
print(prueba.rd)
conteo = 0

for n,row in enumerate(prueba.rd):
    if '~' in row:
        ultima = n
for row in prueba.rd[0:ultima+2]:
    for col in row:
        if col == '|' or col == '-' or col == '~':
            conteo += 1

print(ultima+1)
print(conteo)
print(prueba.childs)
