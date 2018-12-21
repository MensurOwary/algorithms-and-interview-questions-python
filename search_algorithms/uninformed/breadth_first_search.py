"""
Breadth-first algorithm
"""
Graph = dict()
Graph["Arad"] = {"Zerind":75, "Sibiu":140, "Timisoara":118}
Graph["Zerind"] = {"Arad":75, "Oradea":71}
Graph["Oradea"] = {"Zerind":71, "Sibiu":151}
Graph["Sibiu"] = {"Arad":140, "Oradea":151, "Fagaras":99,"Rimnicu Vilcea":80}
Graph["Timisoara"] = {"Arad":118, "Lugoj":111}
Graph["Lugoj"] = {"Timisoara":111, "Mehadia":70}
Graph["Mehadia"] = {"Lugoj":70, "Drobeta":75}
Graph["Drobeta"] = {"Mehadia":75, "Craiova":120}
Graph["Craiova"] = {"Drobeta":120, "Rimnicu Vilcea":146,"Pitesti":138}
Graph["Rimnicu Vilcea"] = {"Sibiu":80, "Craiova":146,"Pitesti":97}
Graph["Pitesti"] = {"Rimnicu Vilcea":97, "Craiova":138,"Bucharest":101}
Graph["Fagaras"] = {"Sibiu":99, "Bucharest":211}
Graph["Bucharest"] = {"Fagaras":211, "Pitesti":101, "Giurgiu":90,"Urziceni":85}
Graph["Giurgiu"] = {"Bucharest":90}
Graph["Urziceni"] = {"Bucharest":85, "Hirsova":98,"Vaslui":142}
Graph["Hirsova"] = {"Urziceni":98, "Eforie":86}
Graph["Eforie"] = {"Hirsova":86}
Graph["Vaslui"] = {"Urziceni":142, "Iasi":92}
Graph["Iasi"] = {"Neamt":87, "Vaslui":92}
Graph["Neamt"] = {"Iasi":87}

Goals = ("Bucharest")

Root = 'Arad'


def breadth_first(start):
    # list to keep track of already visited nodes
    visited = []
    # dictionary of child parent relationship
    parent = {}
    # a queue to pool the next node from
    queue = []
    # add the root node to the queue
    queue.insert(0, start)
    # mark it visited
    visited.append(start)
    # until the queue is empty, proceed
    while len(queue) != 0:
        # take the first node
        node = queue.pop(0)
        # check if it is the Goal state
        if node in Goals:
            # if it is, add it to the visited
            visited.append(node)
            # finish the loop
            break
        # expand the node and take only the ones that are not visited
        expanded = filter_a_list(Graph[node], visited)
        # mark their parent as 'node'
        for exp in expanded:
            parent[exp] = node
        # add them to the queue
        queue.extend(expanded)
        # mark the node as visited
        visited.append(node)
    # return the route
    return show_route(visited, parent)
        
    
# method to return only non visited nodes list
def filter_a_list(l, visited):
    res = []
    for el in l.keys():
        if not visited.__contains__(el):
            res.append(el)
    return res 


# method to find the solution path
def show_route(visited, parent):
    last = visited[-1]
    route = []
    while last != Root:
        route.insert(0, last)
        last = parent[last]
    route.insert(0, last)
    return route   