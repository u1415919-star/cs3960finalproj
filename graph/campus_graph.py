import json

def load_graph(nodes_path="data/nodes.json", edges_path="data/edges.json"):
    with open(nodes_path) as f:
        nodes = json.load(f)
    with open(edges_path) as f:
        edges = json.load(f)

    graph = {node_id: {} for node_id in nodes}
    for edge in edges:
        a, b, w = edge["from"], edge["to"], edge["weight"]
        graph[a][b] = w
        graph[b][a] = w

    return nodes, edges, graph