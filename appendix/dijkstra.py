from typing import List


def dijkstra(edges: List, n: int) -> List:
    graph = [[float('inf') for _ in range(n)] for _ in range(n)]
    visited = [False] * n
    for start, end, weight in edges:
        graph[start][end] = weight

    # assume start point is 0
    costs = graph[0]

    node, cost = find_nearest_node(costs, visited)
    while node:
        neighbors = graph[node]
        for i in range(len(neighbors)):
            costs[i] = min(costs[i], cost + graph[node][i])
        visited[node] = True
        node, cost = find_nearest_node(costs, visited)
    return costs


def find_nearest_node(costs, visited):
    # Could be improved by priority queue (max heap)
    min_cost = float('inf')
    min_node = None
    for i in range(len(costs)):
        if not visited[i] and costs[i] < min_cost:
            min_cost = costs[i]
            min_node = i
    return min_node, min_cost


edges = [
    [0, 1, 6],
    [0, 2, 2],
    [1, 3, 1],
    [2, 1, 3],
    [2, 3, 5],
]

edges = [
    [0, 1, 5],
    [0, 2, 2],
    [1, 3, 4],
    [1, 4, 2],
    [2, 1, 8],
    [2, 4, 7],
    [3, 5, 3],
    [3, 4, 6],
    [4, 5, 1],
]
print(dijkstra(edges, 6))
