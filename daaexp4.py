import heapq


def dijkstra(graph, source):
    """Dijkstra's Algorithm using Min-Heap

    Time: O((V + E) log V), Space: O(V)
    graph: dict {u: [(v, weight), ...]}, 0-indexed
    """
    n = len(graph)
    dist = [float("inf")] * n
    prev = [None] * n
    dist[source] = 0
    pq = [(0, source)]  # (distance, vertex)
    visited = set()

    while pq:
        d, u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)

        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))

    return dist, prev


def reconstruct_path(prev, source, target):
    path = []
    node = target
    while node is not None:
        path.append(node)
        node = prev[node]
    path.reverse()
    if path[0] == source:
        return path
    return []


# --- Modified Graph Definition (Adjacency List) ---
# Weights and connections have been changed
graph = {
    0: [(1, 1), (2, 8)],  # Edge to 1 is now 1 (cheaper than before)
    1: [(3, 2)],  # Edge to 3 is now 2
    2: [(1, 2), (3, 1)],  # Edge to 3 is now 1
    3: [(4, 6)],  # Edge to 4 is now 6
    4: [(5, 4)],  # Edge to 5 is now 4
    5: [],
}

source = 0
dist, prev = dijkstra(graph, source)

print(f"Shortest paths from vertex {source}:")
print(f'{"Vertex":>8} {"Distance":>10} {"Path":>30}')
print("-" * 55)

for v in range(len(graph)):
    path = reconstruct_path(prev, source, v)
    path_str = " -> ".join(map(str, path)) if path else "No path"
    d = dist[v] if dist[v] != float("inf") else "INF"
    print(f"{v:>8} {str(d):>10} {path_str:>30}")