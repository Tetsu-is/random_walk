import random
import graph_tools
import randwalk

def main():
    random.seed()
    
    # Create graph.
    g = graph_tools.Graph(directed=False)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 5)
    g.add_edge(4, 6)
    
    # Create an agent of a given agent class.
    agent = randwalk.SRW(graph=g, current=1)
    
    # Perform an instance of simulation.
    while agent.nvisits[6] == 0:
        print(f't={agent.step}\tv={agent.current}')
        agent.advance()
    
    print(f't={agent.step}\tv={agent.current}')

if __name__ == "__main__":
    main()
