class Path():
    def __init__(self,master_node,rd, goals):
        self.master_node = master_node
        self.rd = rd
        self.current_level = 0
        self.nodes = {self.current_level:[master_node]}
        self.leafs = []
        self.posiciones= [(master_node.x, master_node.y)]
        self.goals = goals
        self.fin = False
        
    def add_node(self,node):
        self.nodes.append(node)
        
    def next_level(self):
        to_add = []
        
        self.nodes[self.current_level+1] = []
        
        for node in self.nodes[self.current_level]:
            for p in node.get_range(self.rd):
                if p not in self.posiciones:
                    
                    child = Node(p[0],p[1],node)
                    node.add_child(child)
                    self.nodes[self.current_level+1].append(child)
                    to_add.append(p)
                    if p in self.goals:
                        child.leaf = True
                        self.leafs.append(child)
                        
        if len(self.nodes[self.current_level+1])==0:
            self.fin = True
        if len(to_add) == 0:
            self.fin = True
        self.posiciones += to_add
        self.current_level += 1
        
    def fill(self):
        while (len(self.leafs) == 0) and (self.fin == False ):
            self.next_level()
        return self.next_move()
    
    def next_move(self):
        if self.fin == True:
            return None

        ne =  sorted([c for 
                       c in self.leafs],
              key = lambda n: (n.get_length(),
                               n.get_y(),n.get_x()))[0]
        return ne.get_x(),ne.get_y()
