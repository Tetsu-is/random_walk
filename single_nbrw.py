import random

class GraphNode:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
        self.visited = False

    def add_neighbor(self,new_neighbor):
        self.neighbors.append(new_neighbor)

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
    
    def advance(self,walker):
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

def main():
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 5)
    g.add_edge(4, 6)

    w = Walker(g, 1)

    #walker advance with specified number of steps
    # for i in range(10):
    #     g.advance(w)
    #     #print time=i and current node
    #     print("Time: ", i, "Current Node: ", w.current)

    #walker advance until walker reaches node 6
    time_count = 0
    while(g.find_node(6).visited == False):
        time_count += 1
        g.advance_nbrw(w)
        print("Time: ", time_count,  "Current Node: ", w.current)
    
    print("Time to reach node 6:", time_count, "steps")


if __name__ == "__main__":
    main()