'''

                                            Experiment No : 07
                                            
                                  Aim:- Implementation of Alpha-Beta Pruning Algorithm
                                                                    
'''                                                                    
import math

def alphabeta(nodeIndex, depth, alpha, beta, isMaximizing, scores):
   # Base case: if depth is 0 or there's only one node left, return its value
   if depth == 0 or len(scores) == 1:
       return scores[0]

   if isMaximizing:
       # If it's the maximizing player's turn, return the maximum value
       bestValue = -math.inf
       for i in range(len(scores) // 2):
           # Recursively call the function for the left child and right child of the current node
           value = alphabeta(nodeIndex * 2 + i, depth - 1, alpha, beta, False, scores)
           # Update the bestValue with the maximum value found so far
           bestValue = max(bestValue, value)
           # Update alpha with the bestValue found so far
           alpha = max(alpha, bestValue)
           # If alpha >= beta, stop exploring this branch of the tree
           if alpha >= beta:
               break
       # Display the final value of alpha
       print("Value of alpha at node", nodeIndex, ":", alpha)
       # Return the bestValue found for this level of the tree
       return bestValue

   else:
       # If it's the minimizing player's turn, return the minimum value
       bestValue = math.inf
       for i in range(len(scores) // 2, len(scores)):
           # Recursively call the function for the left child and right child of the current node
           value = alphabeta(nodeIndex * 2 + i, depth - 1, alpha, beta, True, scores)
           # Update the bestValue with the minimum value found so far
           bestValue = min(bestValue, value)
           # Update beta with the bestValue found so far
           beta = min(beta, bestValue)
           # If alpha >= beta, stop exploring this branch of the tree
           if alpha >= beta:
               break
       # Display the final value of beta
       print("Value of beta at node", nodeIndex, ":", beta)
       # Return the bestValue found for this level of the tree
       return bestValue


scores = [3, 5, 2, 9, 12, 5, 23, 23]
print("The optimal value is:", alphabeta(0, 3, -math.inf, math.inf, True, scores))



'''
Output:-
PS C:\Users\Maazchogle\Desktop\AIlab> & C:/Users/Maazchogle/AppData/Local/Programs/Python/Python311/python.exe c:/Users/Maazchogle/Desktop/AIlab/exp7.py
Value of alpha at node 4 : 3
Value of alpha at node 5 : 3
Value of alpha at node 6 : 3
Value of alpha at node 7 : 3
Value of beta at node 0 : 3
Value of alpha at node 6 : 3
Value of beta at node 1 : 3
Value of alpha at node 8 : 3
Value of beta at node 2 : 3
Value of alpha at node 10 : 3
Value of beta at node 3 : 3
Value of alpha at node 0 : 3
The optimal value is: 3
'''

or

Certainly! Let's break down the code and its logic step by step:

```python
import math

def alphabeta(nodeIndex, depth, alpha, beta, isMaximizing, scores):
   # Base case: if depth is 0 or there's only one node left, return its value
   if depth == 0 or len(scores) == 1:
       return scores[0]
```
Here, we define the `alphabeta` function which implements the alpha-beta pruning algorithm. It takes six parameters:
- `nodeIndex`: The index of the current node in the tree.
- `depth`: The maximum depth of the tree to search.
- `alpha`: The best value that the maximizing player currently can guarantee.
- `beta`: The best value that the minimizing player currently can guarantee.
- `isMaximizing`: A boolean value indicating whether it's the maximizing player's turn or not.
- `scores`: A list containing scores associated with each node in the tree.

If the depth is 0 or there's only one node left, the function returns the value of the only remaining node.

```python
   if isMaximizing:
       # If it's the maximizing player's turn, return the maximum value
       bestValue = -math.inf
       for i in range(len(scores) // 2):
           # Recursively call the function for the left child and right child of the current node
           value = alphabeta(nodeIndex * 2 + i, depth - 1, alpha, beta, False, scores)
           # Update the bestValue with the maximum value found so far
           bestValue = max(bestValue, value)
           # Update alpha with the bestValue found so far
           alpha = max(alpha, bestValue)
           # If alpha >= beta, stop exploring this branch of the tree
           if alpha >= beta:
               break
       # Display the final value of alpha
       print("Value of alpha at node", nodeIndex, ":", alpha)
       # Return the bestValue found for this level of the tree
       return bestValue
```
If it's the maximizing player's turn (`isMaximizing == True`), the function returns the maximum value. It iterates through the child nodes, updating the best value found so far (`bestValue`) and alpha. If alpha is greater than or equal to beta, it stops exploring this branch of the tree.

```python
   else:
       # If it's the minimizing player's turn, return the minimum value
       bestValue = math.inf
       for i in range(len(scores) // 2, len(scores)):
           # Recursively call the function for the left child and right child of the current node
           value = alphabeta(nodeIndex * 2 + i, depth - 1, alpha, beta, True, scores)
           # Update the bestValue with the minimum value found so far
           bestValue = min(bestValue, value)
           # Update beta with the bestValue found so far
           beta = min(beta, bestValue)
           # If alpha >= beta, stop exploring this branch of the tree
           if alpha >= beta:
               break
       # Display the final value of beta
       print("Value of beta at node", nodeIndex, ":", beta)
       # Return the bestValue found for this level of the tree
       return bestValue
```
If it's the minimizing player's turn (`isMaximizing == False`), the function returns the minimum value. It iterates through the child nodes, updating the best value found so far (`bestValue`) and beta. If alpha is greater than or equal to beta, it stops exploring this branch of the tree.

```python
scores = [3, 5, 2, 9, 12, 5, 23, 23]
print("The optimal value is:", alphabeta(0, 3, -math.inf, math.inf, True, scores))
```
Finally, we define the scores list and call the `alphabeta` function with initial parameters. This will print the optimal value obtained using the alpha-beta pruning algorithm.

Output:
```
Value of alpha at node 4 : 3
Value of alpha at node 5 : 3
Value of alpha at node 6 : 3
Value of alpha at node 7 : 3
Value of beta at node 0 : 3
Value of alpha at node 6 : 3
Value of beta at node 1 : 3
Value of alpha at node 8 : 3
Value of beta at node 2 : 3
Value of alpha at node 10 : 3
Value of beta at node 3 : 3
Value of alpha at node 0 : 3
The optimal value is: 3
```
Here, the algorithm prunes several branches of the tree, thus reducing the number of nodes that need to be evaluated, which makes it more efficient than the minimax algorithm.

