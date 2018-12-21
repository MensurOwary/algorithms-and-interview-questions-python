Graph = dict()
Graph["Arad"] = {"Zerind": 75, "Sibiu": 140, "Timisoara": 118}
Graph["Zerind"] = {"Arad": 75, "Oradea": 71}
Graph["Oradea"] = {"Zerind": 71, "Sibiu": 151}
Graph["Sibiu"] = {"Arad": 140, "Oradea": 151, "Fagaras": 99, "Rimnicu Vilcea": 80}
Graph["Timisoara"] = {"Arad": 118, "Lugoj": 111}
Graph["Lugoj"] = {"Timisoara": 111, "Mehadia": 70}
Graph["Mehadia"] = {"Lugoj": 70, "Drobeta": 75}
Graph["Drobeta"] = {"Mehadia": 75, "Craiova": 120}
Graph["Craiova"] = {"Drobeta": 120, "Rimnicu Vilcea": 146,"Pitesti": 138}
Graph["Rimnicu Vilcea"] = {"Sibiu": 80, "Craiova": 146,"Pitesti": 97}
Graph["Pitesti"] = {"Rimnicu Vilcea": 97, "Craiova": 138, "Bucharest": 101}
Graph["Fagaras"] = {"Sibiu": 99, "Bucharest": 211}
Graph["Bucharest"] = {"Fagaras": 211, "Pitesti": 101, "Giurgiu": 90, "Urziceni": 85}
Graph["Giurgiu"] = {"Bucharest": 90}
Graph["Urziceni"] = {"Bucharest": 85, "Hirsova": 98,"Vaslui": 142}
Graph["Hirsova"] = {"Urziceni": 98, "Eforie": 86}
Graph["Eforie"] = {"Hirsova": 86}
Graph["Vaslui"] = {"Urziceni": 142, "Iasi": 92}
Graph["Iasi"] = {"Neamt": 87, "Vaslui": 92}
Graph["Neamt"] = {"Iasi": 87}

Goals = ("Bucharest")

Root = 'Arad'
max_depth = 15

visited = []
parent = {}


# wrapper method
def iterative_deepening_search():
    i = 0
    try:
        for i in range(max_depth):
            iterative_deepening(Root, i)
            visited.clear()
            parent.clear()
        print('No solution')
    except Exception as error:
        print("Solution found at depth", i)
        print(show_route())


def iterative_deepening(start, limit):
    if limit != 0:
        # mark it visited
        visited.append(start)
        # if the node is in goals
        if start in Goals:
            # raise an exception to finish recursion
            raise Exception()
        # otherwise
        else:
            # expand a node and filter out the seen nodes
            expanded = filter_a_list(Graph[start], visited)
            # for each node in the expanded list
            for node in expanded:
                # mark parent as the previous node
                parent[node] = start
                # perform DFS
                iterative_deepening(node, limit-1)


def filter_a_list(l, visited_nodes):
    res = []
    for el in l.keys():
        if not visited_nodes.__contains__(el):
            res.append(el)
    return res


def show_route():
    last = visited[-1]
    route = []
    while last in parent:
        route.insert(0, last)
        last = parent[last]
    route.insert(0, last)
    return route
