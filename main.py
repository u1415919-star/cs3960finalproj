import heapq

def dijkstra(graph, start, end):
    # graph = { 'A': [('B', 5), ('C', 2)], ... }
    
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    prev = {}
    pq = [(0, start)]  # (cost, node)

    while pq:
        cost, node = heapq.heappop(pq)

        if cost > distances[node]:
            continue

        for neighbor, weight in graph[node]:
            new_cost = cost + weight
            if new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                prev[neighbor] = node
                heapq.heappush(pq, (new_cost, neighbor))

    # Reconstruct path
    path = []
    cur = end
    while cur in prev:
        path.append(cur)
        cur = prev[cur]
    path.append(start)
    path.reverse()

    return path, distances[end]


# Example usage
graph = {
    'Library':  [('Plaza', 150),  ('Dorm A', 300)],
    'Plaza':    [('Library', 150),('Gym', 200),    ('Canteen', 100)],
    'Dorm A':   [('Library', 300),('Canteen', 120)],
    'Gym':      [('Plaza', 200),  ('Field', 80)],
    'Canteen':  [('Plaza', 100),  ('Dorm A', 120)],
    'Field':    [('Gym', 80)],
}

path, total = dijkstra(graph, 'Library', 'Field')
print("Path:", " → ".join(path))
print("Distance:", total)