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

Heuristics = dict()
Heuristics["Arad"] = 366
Heuristics["Zerind"] = 374
Heuristics["Oradea"] = 380
Heuristics["Sibiu"] = 253
Heuristics["Timisoara"] = 329
Heuristics["Lugoj"] = 244
Heuristics["Mehadia"] = 241
Heuristics["Drobeta"] = 242
Heuristics["Craiova"] = 160
Heuristics["Rimnicu Vilcea"] = 193
Heuristics["Pitesti"] = 100
Heuristics["Fagaras"] = 176
Heuristics["Bucharest"] = 0
Heuristics["Giurgiu"] = 77
Heuristics["Urziceni"] = 80
Heuristics["Hirsova"] = 151
Heuristics["Eforie"] = 161
Heuristics["Vaslui"] = 199
Heuristics["Iasi"] = 226
Heuristics["Neamt"] = 234


Goal = ['Bucharest']


def greedy(start):
    # we maintain a queue for retrieving a node with minimal heuristics
    queue = dict()
    # child - parent relationship node
    parent = {start: None}
    # list to keep track of already visited nodes
    visited = []
    # add first node with its corresponding heuristics
    queue[start] = Heuristics[start]
    # while queue has elements
    while queue:
        # get the node with minimum cost
        node = min(queue, key=queue.get)
        # if node is a goal
        if node in Goal:
            # return the path and its corresponding cost
            return calculate_path(node, parent)
        # expand the node
        nodes = Graph[node]
        # filter out already visited nodes
        new_nodes = filter_nodes(nodes, visited)
        # loop through the filtered nodes
        for city, cost in new_nodes.items():
            # if node isn't in the queue
            if city not in queue:
                # add it with its corresponding heuristics
                queue[city] = Heuristics[city]
                # set the parent as the expanded node
                parent[city] = node
            # if it already exists with a higher cost tho it is not possible, i think
            if city in queue and queue[city] > Heuristics[city]:
                # replace it with its heuristics
                queue[city] = Heuristics[city]
                # set the parent as the expanded node
                parent[city] = node
        # mark it visited
        visited.append(node)
        # remove the node from queue
        queue.pop(node)


# filters nodes based on if it is already visited
def filter_nodes(nodes, visited):
    result = dict()
    # if city is not visited, add it to the new dictionary
    for city, cost in nodes.items():
        if city not in visited:
            result[city] = Heuristics[city]
    # return result
    return result


# calculate the path
def calculate_path(node, parent):
    last = parent[node]
    route = [node]
    # finds the route
    while last is not None:
        route.append(last)
        last = parent[last]
    route.reverse()
    total = 0
    # finds the cost of the route
    for inx in range(len(route)-1):
        st = route[inx]
        end = route[inx + 1]
        total += Graph[st][end]
    return route, total


if __name__ == '__main__':
    print(greedy('Arad'))