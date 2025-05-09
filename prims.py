import heapq

def prims(graph, start):
    visited = set()
    min_heap = [(0, start)]
    mst_cost = 0

    while min_heap:
        cost, node = heapq.heappop(min_heap)
        if node not in visited:
            visited.add(node)
            mst_cost += cost
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (weight, neighbor))
    
    print("Minimum Cost of MST:", mst_cost)

# Adjacency list: node -> [(neighbor, weight)]
graph = {
    'A': [('B', 1), ('D', 3)],
    'B': [('A', 1), ('C', 4), ('D', 2)],
    'C': [('B', 4), ('D', 5)],
    'D': [('A', 3), ('B', 2), ('C', 5)]
}
prims(graph, 'A')
