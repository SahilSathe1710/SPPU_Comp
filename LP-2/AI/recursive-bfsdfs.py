# graph = {'A':['B','C'],
#          'B':['D','E'],
#          'C':['F','G'],
#          'D':['B'],
#          'E':['B'],
#          'F':['C'],
#          'G':['C'] 
#         }
print("\n")
n = int(input("Enter the number of vertices: "))
graph = {}
for i in range(n):
    vertice_name = input("Enter the name of the vertice: ")
    e = int(input("Enter the no of edges: "))
    edges_list = []
    for j in range(e):
        edge_name = input("Enter the name of the edge: ")
        edges_list.append(edge_name)
    graph.update({vertice_name:edges_list})
print("\n")
print("The Adjacency list is: ", graph)

visited = []
queue = []

def bfs(visited, graph, start_node, goal_node):
    visited.append(start_node)
    queue.append(start_node)
    while queue:
        m = queue.pop(0)
        print(m)
        if m == goal_node:
            print("Goal node achieved!!")
            break
        else:
            for n in graph[m]:
                if n not in visited:
                    visited.append(n)
                    queue.append(n)
print("\n")
print("The BFS traversal is: ")
bfs(visited, graph, 'A', 'G')

visited = []
stack = []

def dfs(graph, start, goal):
    stack.append(start)
    visited.append(start)
    while stack:
        node = stack[-1]
        stack.pop()
        print(node)
        if node == goal:
            print("Goal node achieved!!")
            return
        for n in graph[node]:
                if n not in visited:
                    visited.append(n)
                    stack.append(n)
print("\n")
print("The DFS traversal is: ")
dfs(graph, 'A', 'D')
print("\n")