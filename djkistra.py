import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    min_heap = [(0, start)]

    while min_heap:
        curr_dist, curr_node = heapq.heappop(min_heap)
        for neighbor, weight in graph[curr_node]:
            new_dist = curr_dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(min_heap, (new_dist, neighbor))

    print("Shortest Distances from", start, ":", distances)

graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('A', 2), ('C', 1), ('D', 4)],
    'C': [('A', 5), ('B', 1), ('D', 2)],
    'D': [('B', 4), ('C', 2)]
}
dijkstra(graph, 'A')
