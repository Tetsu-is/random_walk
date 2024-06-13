import random
import rw_module as rw

def main():
    sum = 0
    for i in range(100):
        time_count = 0
        g = rw.Graph()
        g.add_edge(1, 2)
        g.add_edge(1, 3)
        g.add_edge(2, 3)
        g.add_edge(3, 4)
        g.add_edge(4, 5)
        g.add_edge(4, 6)

        w1 = rw.Walker(g, 1)
        w2 = rw.Walker(g, 1)
        while(g.find_node(6).visited == False):
            time_count += 1
            g.advance_together(w1, w2)
            print("Time: ", time_count,  "Current Node1: ", w1.current, "Current Node2: ", w2.current)
    
        print("Time to reach node 6:", time_count, "steps")
        sum += time_count

    print("average time = ", sum/100)


if __name__ == "__main__":
    main()