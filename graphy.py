class Vertex:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}

    def add_neighbor(self, neighbor, weight=0):
        self.connected_to[neighbor] = weight

    def __str__(self):
        return f"{self.id} connectedTo: {[x.id for x in self.connected_to]}"

    def get_connections(self):
        return self.connected_to.keys()

    def get_id(self):
        return self.id

class Graph:
    def __init__(self):
        self.vert_list = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        if key not in self.vert_list:
            self.num_vertices += 1
            self.vert_list[key] = Vertex(key)

    def get_vertex(self, key):
        return self.vert_list.get(key, None)

    def add_edge(self, from_key, to_key, cost=0):
        self.add_vertex(from_key)
        self.add_vertex(to_key)
        self.vert_list[from_key].add_neighbor(self.vert_list[to_key], cost)

    def _dfs(self, vertex, visited, stack):
        visited.add(vertex)
        for neighbor in vertex.get_connections():
            if neighbor not in visited:
                self._dfs(neighbor, visited, stack)
        stack.append(vertex)

    def topological_sort(self):
        visited = set()
        stack = []

        for vertex in self.vert_list.values():
            if vertex not in visited:
                self._dfs(vertex, visited, stack)

        stack.reverse()
        return stack

    def find_path_dfs(self, start, end, path=None):
        if path is None:
            path = []
        start_vertex = self.get_vertex(start)
        if start_vertex is None:
            return None
        path.append(start_vertex)

        if start == end:
            return path

        for neighbor in start_vertex.get_connections():
            if neighbor not in path:
                new_path = self.find_path_dfs(neighbor.get_id(), end, path)
                if new_path:
                    return new_path

        path.pop()
        return None

graph = Graph()
for i in range(4):
    graph.add_vertex(i)

edges = [(0, 1), (0, 2), (1, 3), (2, 3)]
for f, t in edges:
    graph.add_edge(f, t)

sorted_vertices = graph.topological_sort()
print("Топологически отсортированные вершины:", [vertex.get_id() for vertex in sorted_vertices])

path = graph.find_path_dfs(0, 3)
if path:
    print("Путь из 0 в 3:", [vertex.get_id() for vertex in path])
else:
    print("Пути из 0 в 3 не существует.")