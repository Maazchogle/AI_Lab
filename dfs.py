'''
                                        
                                                Experiment No : 03
                                    AIM : Implementation of DFS Algorithmm

                                                                                                        @Learner: TE-CO
                                                                                                        Name: Maaz Aslam Chogle 
                                                                                                        Roll No: 21CO19
                                                                                                        Batch: 1
                                                                                                        Academic Year: 2023- 2024
                                                                                                        Sem - 6
                                                                                                        
'''
# Using a Python dictionary to act as an adjacency list
graph = {
  'M' : ['A','Z'],
  'A' : ['S', 'L'],
  'Z' : ['C'],
  'S' : [],
  'L' : ['C'],
  'C' : []
}


visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, 'M')


# sh-5.1$ /bin/python /home/aiktc/Desktop/m/dfs.py
# Following is the Depth-First Search
# M
# A
# S
# L
# C
# Z