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
    queue = {start: 0}
    visited = dict()
    parents = {start: start}
    while queue:
        node = min(queue, key=queue.get)
        visited[node] = calculate_path(node, parents, start) + Heuristics[node]
        if node in Goal:
            route = show_route(node, parents, start)
            route.append(node)
            return route
        # filter the nodes and add them to the queue
        filter_nodes(node, visited, parents, start, queue)
        queue.pop(node)
    return []


def filter_nodes(node, visited, parents, start, queue):
    """
        {"Arad":140, "Oradea":151, "Fagaras":99,"Rimnicu Vilcea":80}
    """

    cost_so_far = calculate_path(node, parents, start)
    nodes = Graph[node]
    for city, cost in nodes.items():
        overall_city_cost = cost_so_far + cost + Heuristics[city]
        if city not in visited:
            queue[city] = overall_city_cost
            parents[city] = node
        elif visited[city] > overall_city_cost or (city in queue and queue[city] > overall_city_cost):
            queue[city] = overall_city_cost
            parents[city] = node


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


