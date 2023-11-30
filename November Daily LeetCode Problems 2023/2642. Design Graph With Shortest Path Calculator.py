import heapq

class Graph:
    def __init__(self, n, edges):
        self.graph = {i: [] for i in range(n)}
        for edge in edges:
            from_node, to_node, cost = edge
            self.graph[from_node].append((to_node, cost))

    def addEdge(self, edge):
        from_node, to_node, cost = edge
        self.graph[from_node].append((to_node, cost))

    def shortestPath(self, node1, node2):
        heap = [(0, node1)]  # (cost, node)
        visited = set()

        while heap:
            current_cost, current_node = heapq.heappop(heap)

            if current_node in visited:
                continue

            visited.add(current_node)

            if current_node == node2:
                return current_cost

            for neighbor, edge_cost in self.graph[current_node]:
                if neighbor not in visited:
                    heapq.heappush(heap, (current_cost + edge_cost, neighbor))

        return -1

