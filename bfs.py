'''
                                        
                                             Experiment No : 03
                                     AIM : Implementation of BFS Algorithmm

                                                                                                       
                                                                                                      
                                                                                                        
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

Another 
from collections import deque

def bfs(graph, start_node):
    """
    Performs BFS traversal on a graph.

    Args:
        graph (dict): The graph represented as an adjacency dictionary.
        start_node: The starting node for traversal.

    Returns:
        list: List of nodes visited in BFS order.
    """
    visited = set()  # Set to keep track of visited nodes
    queue = deque([start_node])  # Initialize the queue with the start node
    result = []  # List to store the BFS traversal order

    while queue:
        current_node = queue.popleft()  # Get the next node from the queue
        if current_node not in visited:
            visited.add(current_node)  # Mark the node as visited
            result.append(current_node)  # Add it to the result list

            # Enqueue all unvisited neighbors of the current node
            for neighbor in graph.get(current_node, []):
                if neighbor not in visited:
                    queue.append(neighbor)

    return result

# Example usage
if __name__ == "__main__":
    # Define an example graph (adjacency dictionary)
    example_graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    start_node = 'A'
    bfs_order = bfs(example_graph, start_node)
    print("BFS traversal starting from node", start_node, ":", bfs_order)

op: 

BFS traversal starting from node A : ['A', 'B', 'C', 'D', 'E', 'F']

[Done] exited with code=0 in 0.073 seconds
