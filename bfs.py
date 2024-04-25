'''
                                        
                                             Experiment No : 03
                                     AIM : Implementation of BFS Algorithmm

                                                                                                        @Learner: TE-CO
                                                                                                        Name: Maaz Aslam Chogle 
                                                                                                        Roll No: 21CO19
                                                                                                        Batch: 1
                                                                                                        Academic Year: 2023- 2024
                                                                                                        Sem - 6
                                                                                                        
'''
graph = {
  'M' : ['A','Z'],
  'A' : ['S', 'L'],
  'Z' : ['C'],
  'S' : [],
  'L' : ['C'],
  'C' : []
}

visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph, 'M')    # function calling

# sh-5.1$ /bin/python /home/aiktc/Desktop/m/bfs.py
# Following is the Breadth-First Search
# M A Z S L C sh-5.1$ ^C
# sh-5.1$ 