class Player():
    def __init__(self,name):
        self.name = name
        self.marbles = []
        self.score = 0
        
    def add_score(self, marble):
        self.score += marble
        
class Marble():
    def __init__(self, value):
        self.value = value
        self.position = None
        
    def set_position(self,position):
        self.position = position
        

        
class Circle():
    def __init__ (self, numMarbles, numPlayers):
        self.positions = []
        self.numMarbles = numMarbles
        self.numPlayers = numPlayers
        self.players = []
        self.marbles = []
        
    def initPlayers(self):
        for i in range(self.numPlayers):
            self.players.append(Player(i))
        
    def initMarbles(self):
        for i in range(self.numMarbles):
            self.marbles.append(Marble(i))

            
    def dealMarbles(self):
        for k,marb in enumerate(self.marbles):
            while k >= len(self.players):
                k -= self.numPlayers
            self.players[k].marbles.append(marb)
            
    def play(self):
        for turno in range(self.numMarbles):
            while turno >= len(self.players):
                turno -= self.numPlayers
            canica = self.players[turno].marbles.pop(0)
            if self.positions == []:
                self.positions.append(canica)
                current_marble = canica
                print('turno ',turno, 'positions ', self.positions)
                continue
                
            
            if len(self.positions)<2:
                self.positions.append(canica)
                current_marble = canica
                print('turno ',turno, 'positions ', self.positions)
                continue
                
            if len(self.positions)>=2:

                index_current = self.positions.index(current_marble)
                if canica.value % 23 != 0:
                    if index_current+2 == len(self.positions):
                        self.positions.append(canica)
                        current_marble = canica
                        continue
                    if index_current+2 <len(self.positions):
                        self.positions.insert(index_current+2,canica)
                        current_marble = canica
                        continue
                    if index_current+2 >len(self.positions):
                        self.positions.insert(1,canica)
                        current_marble = canica
                        continue
                if canica.value % 23 == 0:
                    self.players[turno].add_score(canica.value)
                    try:
                        remover = self.positions[self.positions.index(current_marble)-7]
                    except:
                        remover = self.positions[self.positions.index(current_marble)-7+len(self.positions)]
                    self.players[turno].add_score(remover.value)
                    try:
                        current_marble = self.positions[self.positions.index(remover)+1]
                    except:
                        current_marble = self.positions[self.positions.index(remover)+1-len(self.positions)]
                    self.positions.pop(self.positions.index(remover))

                    
myCircle = Circle(7090400,473)
myCircle.initPlayers()
myCircle.initMarbles()
myCircle.dealMarbles()
myCircle.play()
print(max([i.score for i in myCircle.players]))
