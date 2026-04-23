import heapq

def dijkstra(graph: dict, start: str, end: str):
    dist = {node: float("inf") for node in graph}
    prev = {node: None for node in graph}
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        cost, u = heapq.heappop(heap)
        if u == end:
            break
        if cost > dist[u]:
            continue
        for v, w in graph[u].items():
            new_cost = cost + w
            if new_cost < dist[v]:
                dist[v] = new_cost
                prev[v] = u
                heapq.heappush(heap, (new_cost, v))

    path, node = [], end
    while node:
        path.append(node)
        node = prev[node]
    return list(reversed(path)), dist[end]