"""
Uniform cost search
"""

# Graph = dict()
# Graph["S"] = {"A": 5, "B": 9, "D": 6}
# Graph["A"] = {"G1": 9, "B": 3}
# Graph["B"] = {"A": 2, "C": 1}
# Graph["C"] = {"S": 6, "G2": 5, "F": 7}
# Graph["D"] = {"S": 1, "C": 2, "E": 2}
# Graph["E"] = {"G3": 7}
# Graph["F"] = {"D": 2, "G3": 8}
# Graph['G1'] = {"A": 9}
# Graph['G2'] = {"C": 5}
# Graph['G3'] = {"E": 7, "F": 8}
#
# Goals = ('G1', 'G2', 'G3')
#
# Root = 'S'

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


def uniform_cost_search(start):
    # keep track of which nodes are visited
    visited = []
    # parent child relationship map
    parent = {}
    # priority queue
    # and initially, the root has 0 cost
    queue = {start: 0}
    # until the queue is empty, proceed
    while len(queue) != 0:
        # take the node with minimum cost
        node = min(queue, key=queue.get)
        # mark it visited
        visited.append(node)
        # if it is one of goals
        if node in Goals:
            # finish the loop
            break
        # expand its children, but exclude already visible ones
        expanded = filter_a_list(Graph[node], visited)
        # for each node and its own cost
        for k, v in expanded.items():
            # if element is already in queue
            # but has higher value
            # replace it with new one
            if k in queue and queue[k] > queue[node] + v:
                queue[k] = queue[node] + v
                parent[k] = node
            # if it is not, add it
            if k not in queue:
                queue[k] = queue[node] + v
                parent[k] = node
        # remove the node from the queue
        queue.pop(node)
    # return cost and the path
    return calc_cost(visited, parent)


# method to return only non visited nodes list
def filter_a_list(l, visited):
    res = {}
    for k, v in l.items():
        if not visited.__contains__(k):
            res[k] = v
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


def calc_cost(visited, parent):
    route = show_route(visited, parent)
    total = 0
    for i in range(len(route)-1):
        total = total + Graph[route[i]][route[i+1]]
    return total, route
