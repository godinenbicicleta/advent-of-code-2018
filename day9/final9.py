from collections import deque
import datetime
class Player():
    def __init__(self,name):
        self.name = name
        self.score = 0

    def add_score(self, marble):
        self.score += marble

class Marble():
    def __init__(self, value):
        self.value = value

class Circle():
    def __init__ (self, numMarbles, numPlayers):
        self.positions = {i:deque() for i in range(numMarbles+1)}
        self.numMarbles = numMarbles
        self.numPlayers = numPlayers
        self.players = {i:0 for i in range(numPlayers)}



    def play(self):
        posiciones_ocupadas = 0
        current_index = 0
        #we need as many turns as marbles+1, no way of chaning that...
        for turno in range(self.numMarbles+1):
            if turno%1000 == 0:
                print(turno, end = ', ')
            #print(turno,current_index+2,posiciones_ocupadas,self.positions)


            #select which player is up next
            jugador = turno
            while jugador >= len(self.players):
                jugador -= self.numPlayers

            #now turno is the player's id

            if turno == 0:
                current_index = 0
                posiciones_ocupadas = 1
                self.positions[0].append(0)
                continue


            if posiciones_ocupadas == 1:
                self.positions[1].append(1)
                current_index = 1
                posiciones_ocupadas += 1

                continue

            if posiciones_ocupadas>=2:
                #en el loop 0 current_index = 1

                if turno % 23 != 0:
                    if current_index+2 == posiciones_ocupadas:
                        self.positions[current_index+2].append(turno)
                        posiciones_ocupadas +=1

                        current_index +=2
                        continue

                    if current_index+2 < posiciones_ocupadas:
                        # de index_current+2 en adelante tengo que recorrerlos 1
                        #para todos los que estan a la derecha
                        for k in range(current_index+2+1,posiciones_ocupadas+1):
                            self.positions[k].append(self.positions[k-1].popleft())


                        #ahora si inserto index_current+2
                        self.positions[current_index+2].append(turno)

                        posiciones_ocupadas+=1
                        current_index+=2
                        continue

                    if current_index+2 > posiciones_ocupadas:
                        posi = current_index+2
                        while posi>posiciones_ocupadas:
                            posi-=posiciones_ocupadas
                        #de posi en adelante, hay que recorrerlos

                        for k in range(posi+1,posiciones_ocupadas+1):
                            self.positions[k].append(self.positions[k-1].popleft())
                            self.positions[posi].append(turno)

                        current_index = posi
                        posiciones_ocupadas+=1

                        continue

                if turno % 23 == 0:
                    self.players[jugador]+= turno

                    if current_index-7>=0:


                        #sumarle la canica al jugador
                        self.players[jugador]+= self.positions[current_index-7].pop()
                        posiciones_ocupadas-=1
                        #hay que quitar la canica en index_current-7
                        #de posi en adelante, hay que recorrerlos


                        for k in range(current_index-7,posiciones_ocupadas):
                            self.positions[k].append(self.positions[k+1].popleft())





                        current_index = current_index-7
                        continue

                    if current_index-7<0:
                        #print(turno,current_index+2,posiciones_ocupadas,self.positions)
                        #sumarle la canica al jugador
                        #print('voy a popear',current_index-7+posiciones_ocupadas)
                        self.players[jugador]+= self.positions[current_index-7+posiciones_ocupadas].pop()
                        #print(self.positions)
                        posiciones_ocupadas-=1
                        #hay que quitar la canica en index_current-7

                        #hay que rellenar el vacio

                        for k in range(current_index-7+posiciones_ocupadas+1,posiciones_ocupadas):
                            self.positions[k].append(self.positions[k+1].popleft())
                            current_index = current_index-7+posiciones_ocupadas+1

                        continue


import datetime
myCircle = Circle(7090400,473)
a = datetime.datetime.now()

myCircle.play()

with open('day9_resultado.text','w') as f:
    f.write(str(sorted(list(myCircle.players.items()),
    key = lambda x: x[1],reverse = True)[0]))
    f.write(str(datetime.datetime.now()-a))

f.close()
