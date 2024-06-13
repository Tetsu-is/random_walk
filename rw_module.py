import random

class GraphNode:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
        self.visited = False

    def add_neighbor(self,new_neighbor):
        self.neighbors.append(new_neighbor)

    def clear_visited(self):
        self.visited = False

class Graph:
    def __init__(self):
        self.nodes = [] #list of nodes

    def add_edge(self, val1, val2):
        node1 = self.find_node(val1)
        if (node1 == None):
            node1 = GraphNode(val1)
            self.nodes.append(node1)

        node2 = self.find_node(val2)
        if (node2 == None):
            node2 = GraphNode(val2)
            self.nodes.append(node2) 

        node1.add_neighbor(node2)
        node2.add_neighbor(node1)


    def find_node(self, value):
        for node in self.nodes:
            if node.value == value:
                return node
        return None
    
    def reset_history(self):
        for node in self.nodes:
            node.clear_visited()

    def check_node_visited(self, value):
        for node in self.nodes:
            if node.value == value:
                return node.visited
        return None



    def advance(self,walker):
        neighbors = walker.graph.find_node(walker.current).neighbors
        walker.current = neighbors[random.randint(0,len(neighbors)-1)].value
        walker.graph.find_node(walker.current).visited = True
    
    def advance_together(self, *walkers):
        for walker in walkers:
            neighbors = walker.graph.find_node(walker.current).neighbors
            walker.current = neighbors[random.randint(0,len(neighbors)-1)].value
            walker.graph.find_node(walker.current).visited = True

    def advance_nbrw(self,walker):
        neighbors = walker.graph.find_node(walker.current).neighbors
        next_node = neighbors[random.randint(0,len(neighbors)-1)].value

        while (next_node == walker.last_node and len(neighbors) > 1):
            print("retrying...")
            next_node = neighbors[random.randint(0,len(neighbors)-1)].value
        
        walker.last_node = walker.current
        walker.current = next_node
        walker.graph.find_node(walker.current).visited = True
            
    

class Walker:
    def __init__(self, graph, current):
        self.graph = graph
        self.current = current
        self.last_node = None

    def reset(self, graph, current):
        self.graph = graph
        self.current = current
        self.last_node = None