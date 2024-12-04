def bs_insert(lst, item):
    l, r = 0, len(lst) - 1
    while l <= r:
        m = (l + r) // 2
        if lst[m][0] < item[0]:
            l = m + 1
        else:
            r = m - 1
    lst.insert(l, item)

class Graph:
    def __init__(self, n):
        self.n = n
        self.dots = [[] for _ in range(n)]

    def add_road(self, u, v, weight):
        self.dots[u].append((v, weight))
        self.dots[v].append((u, weight))

    def dijkstra(self, start):
        distances = [1000001] * self.n
        distances[start] = 0
        q = [(0, start)]

        while q:
            current_distance, current_dot = q.pop(0)

            if current_distance > distances[current_dot]:
                continue

            for neighbor, weight in self.dots[current_dot]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    bs_insert(q, (distance, neighbor))

        return distances
    
    def _fw(self):
        matrix = [[1000001] * self.n for _ in range(self.n)]

        for i in range(self.n):
            matrix[i][i] = 0
        
        for u in range(self.n):
            for v, weight in self.dots[u]:
                matrix[u][v] = weight
        
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                        matrix[i][j] = matrix[i][k] + matrix[k][j]
        
        return matrix
    
    def find_center(self):
        matrix = self._fw()

        min_max = 1000001
        center = 0

        for i in range(self.n):
            _max = max(matrix[i])
            if _max < min_max:
                min_max = _max
                center = i

        return center

# n, m, k, c = map(int, input().split())
# cities = list(map(int, input().split()))

# graph = Graph(n)

# for _ in range(m):
#     u, v, weight = map(int, input().split())
#     graph.add_road(u - 1, v - 1, weight)

# distances = graph.dijkstra(c - 1)

# for city in cities:
#     print(city, distances[city - 1])

n, m = map(int, input().split())
graph = Graph(n)

for _ in range(m):
    u, v, weight = map(int, input().split())
    graph.add_road(u - 1, v - 1, weight)

print(graph.find_center() + 1)