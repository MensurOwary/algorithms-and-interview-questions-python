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


def a_star(start):
    # initialize a queue with the start point being the only element in it
    # its cost is equal to its heuristics
    queue = {start: Heuristics[start]}
    # dictionary to keep track of visited nodes
    visited = dict()
    # dictionary to keep track of child - parent relationship
    parents = {start: start}
    # while the queue is not empty
    while queue:
        # take the node with minimum cost
        node = min(queue, key=queue.get)
        # add it to the visited dictionary
        # its total cost will be path until the node + its heuristic cost
        visited[node] = calculate_path(node, parents, start) + Heuristics[node]
        # if the node is goal node
        if node in Goal:
            # return the path
            route = show_route(node, parents, start)
            route.append(node)
            return route
        # filter the nodes and add them to the queue
        filter_nodes(node, visited, parents, start, queue)
        # remove the node from the queue
        queue.pop(node)
    # if no path found return an empty list
    return []


# filters nodes based on the visited list
def filter_nodes(node, visited, parents, start, queue):
    # cost from the start node to the current node
    cost_so_far = calculate_path(node, parents, start)
    # children nodes
    nodes = Graph[node]
    # for each expanded node
    for city, cost in nodes.items():
        # calculate overall city cost
        # it is equal to
        # 1. cost_so_far - the path cost from start node to the current node
        # 2. cost - the cost of reaching the node itself from the parent node
        # 3. Heuristics[city] - heuristic cost of the node
        overall_city_cost = cost_so_far + cost + Heuristics[city]
        # if the node is not visited
        if city not in visited:
            # add it to the queue with total cost
            queue[city] = overall_city_cost
            # set its parent to the node that expanded it
            parents[city] = node
        # if it is visited but for higher cost than the current one
        elif visited[city] > overall_city_cost or (city in queue and queue[city] > overall_city_cost):
            # add it to the queue with total cost
            queue[city] = overall_city_cost
            # set its parent to the node that expanded it
            parents[city] = node


# calculate the path cost
def calculate_path(node, parents, start):
    route = show_route(node, parents, start)
    total = 0
    for i in range(len(route) - 1):
        total = total + Graph[route[i]][route[i + 1]]
    return total


# method to find the solution path
def show_route(node, parents, start):
    last = parents[node]
    route = []
    while last != start:
        route.insert(0, last)
        last = parents[last]
    route.insert(0, last)
    return route


if __name__ == "__main__":
    res = a_star("Arad")
    print(res)


