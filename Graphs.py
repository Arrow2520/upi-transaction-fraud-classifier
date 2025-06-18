class Graph:
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        self.data = [[] for _ in range(num_nodes)]
        for n1, n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)

    def __repr__(self):
        return "\n".join(["{}: {}".format(n, neighbours) for n, neighbours in enumerate(self.data)])

    def __str__(self):
        return self.__repr__()


num_nodes = 5
edges = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)]
graph1 = Graph(num_nodes, edges)


def bfs(graph, root):
    queue = []
    discovered = [False] * len(graph.data)
    distance = [None] * len(graph.data)
    parent = [None] * len(graph.data)

    discovered[root] = True
    distance[root] = 0
    queue.append(root)
    idx = 0

    while idx < len(queue):
        current = queue[idx]
        idx += 1
        for node in graph.data[current]:
            if not discovered[node]:
                distance[node] = 1 + distance[current]
                parent[node] = current
                discovered[node] = True
                queue.append(node)
    return queue, distance, parent


def dfs(graph, root):
    stack = []
    discovered = [False] * len(graph.data)
    result = []
    stack.append(root)

    while len(stack) > 0:
        current = stack.pop()
        if not discovered[current]:
            discovered[current] = True
            result.append(current)
            for node in graph.data[current]:
                if not discovered(node):
                    stack.append(node)
    return result


class Graph2:
    def __init__(self, num_nodes, edges, directed=False, weighted=False):
        self.num_nodes = num_nodes
        self.directed = directed
        self.weighted = weighted
        self.data = [[] for _ in range(num_nodes)]
        self.weight = [[] for _ in range(num_nodes)]
        for edge in edges:
            if self.weighted:
                node1, node2, weight = edge
                self.data[node1].append(node2)
                self.weight[node1].append(weight)
                if not directed:
                    self.data[node2].append(node1)
                    self.weight[node2].append(weight)
            else:
                node1, node2 = edge
                self.data[node1].append(node2)
                if not directed:
                    self.data[node2].append(node1)

    def __repr__(self):
        result = ""
        if self.weighted:
            for i, (nodes, weights) in enumerate(zip(self.data, self.weight)):
                result += "{}: {}\n".format(i, list(zip(nodes, weights)))
        else:
            for i, nodes in enumerate(self.data):
                result += "{}: {}\n".format(i, nodes)
        return result

    def __str__(self):
        return self.__repr__()


# Next part is for Sorting Algorithms
num_nodes5 = 6
edges5 = ((0, 1, 4), (0, 2, 2), (1, 3, 10), (1, 2, 5), (2, 4, 3), (4, 3, 4), (3, 5, 11))
graph5 = Graph2(num_nodes5, edges5, True, True)
print(graph5)


def update_distances(graph, current, distance, parent=None):
    neighbors = graph.data[current]
    weights = graph.weight[current]
    for i, node in enumerate(neighbors):
        weight = weights[i]
        if distance[current] + weight < distance[node]:
            distance[node] = distance[current] + weight
            if parent:
                parent[node] = current


def pick_next_node(distance, visited):
    min_distance = float('inf')
    min_node = None
    for node in range(len(distance)):
        if not visited[node] and distance[node] < min_distance:
            min_node = node
            min_distance = distance[node]
    return min_node


def shortest_path(graph, source, target):
    visited = [False] * len(graph.data)
    parent = [None] * len(graph.data)
    distance = [float('inf')] * len(graph.data)
    queue = []
    distance[source] = 0
    queue.append(source)
    idx = 0
    while idx < len(queue) and not visited[target]:
        current = queue[idx]
        idx += 1
        visited[current] = True
        update_distances(graph, current, distance, parent)
        next_node = pick_next_node(distance, visited)
        if next_node:
            queue.append(next_node)
    return distance[target], parent