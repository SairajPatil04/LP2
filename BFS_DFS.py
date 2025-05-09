from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = set()

    # Add an undirected edge
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    # Recursive DFS
    def dfs(self, node):
        if node not in self.visited:
            print(node, end=' ')
            self.visited.add(node)
            for neighbor in self.graph[node]:
                self.dfs(neighbor)

    # Iterative BFS
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            node = queue.popleft()
            print(node, end=' ')
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

    # Reset visited nodes for DFS
    def reset(self):
        self.visited.clear()

# Main program with menu
def main():
    g = Graph()

    while True:
        print("\n=== Graph Menu ===")
        print("1. Add Edge")
        print("2. Display Graph")
        print("3. DFS (Recursive)")
        print("4. BFS")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            u = input("Enter first node: ")
            v = input("Enter second node: ")
            g.add_edge(u, v)
            print(f"Edge added: {u} -- {v}")

        elif choice == '2':
            print("\nGraph:")
            for node in g.graph:
                print(f"{node} -> {g.graph[node]}")

        elif choice == '3':
            start = input("Enter starting node for DFS: ")
            g.reset()
            print("DFS Traversal:")
            g.dfs(start)
            print()

        elif choice == '4':
            start = input("Enter starting node for BFS: ")
            print("BFS Traversal:")
            g.bfs(start)
            print()

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
