def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    else:
        parent[yroot] = xroot
        if rank[xroot] == rank[yroot]:
            rank[xroot] += 1

def kruskal(nodes, edges):
    edges.sort(key=lambda x: x[2])
    parent = {node: node for node in nodes}
    print(parent)
    rank = {node: 0 for node in nodes}
    mst = []

    for u, v, weight in edges:
        if find(parent, u) != find(parent, v):
            mst.append((u, v, weight))
            union(parent, rank, u, v)

    print("Edges in MST:", mst)

nodes = ['A', 'B', 'C', 'D']
edges = [('A', 'B', 1), ('B', 'C', 4), ('A', 'D', 3), ('B', 'D', 2), ('C', 'D', 5)]
kruskal(nodes, edges)
