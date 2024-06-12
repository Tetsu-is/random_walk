import random
import graph_tools
import randwalk

def rand():
    random.seed()
    
    # Create graph.
    g = graph_tools.Graph(directed=False)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 5)
    g.add_edge(4, 6)
    
    # Create an agent of a given agent class.
    # agent = randwalk.SRW(graph=g, current=1)
    agent = randwalk.BloomRW(graph=g, current=1)
    
    # Perform an instance of simulation.
    while agent.nvisits[6] == 0:
        print(f't={agent.step}\tv={agent.current}')
        agent.advance()
    
    return agent.step

def main():
    result_arr = []
    count = 0

    for i in range(100):
        result_arr.append(rand())
        if result_arr[i] <= 10:
            print("this is less than 10--------------------------!!!!\n", result_arr[i])
            count += 1

    avg = sum(result_arr) / len(result_arr)
    print(avg)
    print("how many times less than 10: ", count)

if __name__ == "__main__":
    main()
