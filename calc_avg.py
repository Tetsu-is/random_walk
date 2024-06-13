import rw_module as rw


def main():
    t = 0
    sum_t = 0

    # Create a graph
    g = rw.Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 5)
    g.add_edge(4, 6)

    # simple random walk
    w = rw.Walker(g, 1)

    for i in range(100):
        t = 0
        while g.find_node(6).visited == False:
            t += 1
            g.advance(w)
        sum_t += t
        w.reset(g,1)
        g.reset_history()
    print("[simple random work]Average:", sum_t/100, "steps")

    del w

    # non-back random walk
    w = rw.Walker(g, 1)
    for i in range(100):
        t = 0
        while g.find_node(6).visited == False:
            t += 1
            g.advance_nbrw(w, False)
        sum_t += t
        w.reset(g,1)
        g.reset_history()


if __name__ == "__main__":
    main()
