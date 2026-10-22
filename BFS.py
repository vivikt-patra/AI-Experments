from collections import deque

#Function to perform BFS
def bfs(graph, start):
    visited=set()
    queue= deque([start])
    visited.add(start)

    print("BFS Traversal:", end=" ")

    while queue:
            vertex=queue.popleft()
            print(vertex, end=" ")
        
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

#Main Program
graph={}
n=int(input("Enter the no. of the vertices: "))

for i in range(n):
        vertex=input(f"Enter vertex{i+1}: ")
        neighbors=input(
              f"enter adjacent vertices of {vertex} (space-separated): ").split()
        graph[vertex]= neighbors

start= input("Enter the starting vertex: ")

print("\nGraph: ",graph )
bfs(graph,start)

#output
'''
Enter the no. of the vertices: 4
Enter vertex1: A
enter adjacent vertices of A (space-separated): B C
Enter vertex2: B
enter adjacent vertices of B (space-separated): A D
Enter vertex3: C
enter adjacent vertices of C (space-separated): A D
Enter vertex4: D
enter adjacent vertices of D (space-separated): B C
Enter the starting vertex: A

Graph:  {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'D'], 'D': ['B', 'C']}
BFS Traversal: A B C D 
'''